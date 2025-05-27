import sys, re
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession, functions as F, types as T
from pyspark.sql import Window
from awsglue.context import GlueContext
from awsglue.job import Job

#parâmetros do Glue 
args = getResolvedOptions(
    sys.argv,
    ["JOB_NAME", "TRUSTED_CSV_PATH", "TRUSTED_JSON_PATH", "REFINED_PATH"]
)

#  sessão Spark / Glue
spark = SparkSession.builder.getOrCreate()
glue_ctx = GlueContext(spark.sparkContext)
job = Job(glue_ctx)
job.init(args["JOB_NAME"], args)

refined_root = re.sub(r"/?$", "/", args["REFINED_PATH"].strip())


# 1. DIM_FILME 
df_csv = (
    spark.read
         .option("recursiveFileLookup", "true")
         .parquet(args["TRUSTED_CSV_PATH"])
         .select(
             F.col("id").alias("imdb_id"),
             F.col("tituloPincipal").alias("titulo_principal"),
             F.col("tituloOriginal").alias("titulo_original"),
             F.col("anoLancamento").cast("int").alias("ano_lancamento"),
             F.col("tempoMinutos").cast("int").alias("tempo_minutos"),
             "genero",
             F.col("notaMedia").cast("double").alias("nota_media"),
             F.col("numeroVotos").cast("int").alias("numero_votos"),
         )
)

dim_filme = (
    df_csv.dropDuplicates(["imdb_id"])
          .withColumn("filme_sk", F.row_number().over(Window.orderBy("imdb_id")))
)

(dim_filme.write
         .mode("overwrite")
         .parquet(f"{refined_root}dim_filme/"))

# 2. DIM_ESTUDIO  +  BRIDGE_FILME_ESTUDIO  (fonte JSON TMDB)

# lemos apenas as colunas necessárias
df_json = (
    spark.read
         .option("recursiveFileLookup", "true")
         .parquet(args["TRUSTED_JSON_PATH"])
         .select("imdb_id", "production_companies")
         .filter(F.col("imdb_id").isNotNull())
)

# Produz um array de strings
studios_inter = (
    df_json
      .withColumn(
          "pc_array",
          F.when(                               # se já for ARRAY -> mantém
              F.col("production_companies").cast("array<string>").isNotNull(),
              F.col("production_companies").cast("array<string>")
          )
          # senão… considera que é STRING no formato "[A, B, C]"
          .otherwise(
              F.split(
                  F.regexp_replace(
                      F.col("production_companies").cast("string"),
                      r"^\[|\]$", ""
                  ),
                  r"\s*,\s*"
              )
          )
      )
      .select("imdb_id", F.explode_outer("pc_array").alias("nome_estudio_raw"))
      .withColumn("nome_estudio", F.trim("nome_estudio_raw"))
      .filter(F.col("nome_estudio") != "")
      .select("imdb_id", "nome_estudio")
)

#dim_estudio 
dim_estudio = (
    studios_inter.select("nome_estudio")
                 .dropDuplicates()
                 .withColumn(
                     "estudio_sk",
                     F.row_number().over(Window.orderBy("nome_estudio"))
                 )
)

(dim_estudio.write
            .mode("overwrite")
            .parquet(f"{refined_root}dim_estudio/"))

#── bridge filme × estúdio ────────────────────────────────────────────────────
bridge_filme_estudio = (
    studios_inter
        .join(dim_filme,  "imdb_id")
        .join(dim_estudio, "nome_estudio")
        .select("filme_sk", "estudio_sk")
        .dropDuplicates()
)

(bridge_filme_estudio.write
                     .mode("overwrite")
                     .parquet(f"{refined_root}bridge_filme_estudio/"))


# 3. DIM_TEMPO (por DÉCADA a partir do ano_lancamento)

decadas_df = (
    df_csv.select("ano_lancamento")
          .where("ano_lancamento IS NOT NULL AND ano_lancamento > 1800")
          .withColumn("decada", (F.col("ano_lancamento")/10).cast("int")*10)
          .select("decada")
          .dropDuplicates()
)

dim_tempo = (
    decadas_df
      .withColumn("tempo_sk", F.col("decada"))
      .select("tempo_sk", "decada")
      .orderBy("decada")
)

(dim_tempo.write
          .mode("overwrite")
          .parquet(f"{refined_root}dim_tempo/"))

job.commit()
