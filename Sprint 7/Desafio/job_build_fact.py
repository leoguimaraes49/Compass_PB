import sys
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession, functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

# parâmetros 
args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME',
     'REFINED_PATH',          
     'TRUSTED_JSON_PATH',      
     'REFINED_FACT_PATH']     
)

spark = SparkSession.builder.getOrCreate()
glue  = GlueContext(spark.sparkContext)
job   = Job(glue)
job.init(args['JOB_NAME'], args)

dim_filme = spark.read.parquet(f"{args['REFINED_PATH']}/dim_filme/")
dim_tempo = spark.read.parquet(f"{args['REFINED_PATH']}/dim_tempo/")

#2. lê métricas
df_json = (spark.read
           .option("recursiveFileLookup", "true")
           .parquet(args['TRUSTED_JSON_PATH'])
           .select("imdb_id",
                   F.col("budget").cast("double").alias("budget"),
                   F.col("revenue").cast("double").alias("revenue"))
           .filter("imdb_id IS NOT NULL"))

# 3. monta fato básica 
fact = (df_json.alias("j")
        .join(dim_filme.alias("f"), "imdb_id")# fk filme
        .withColumn("decada", (F.col("ano_lancamento")/10).cast("int")*10)
        .join(dim_tempo.alias("t"), "decada", "left")  # fk tempo
        .select(F.col("f.filme_sk"),
                F.col("t.tempo_sk"),
                "budget", "revenue")  
        )

fact = (fact
        .withColumn("budget",
                    F.when(F.col("budget")==0,   None).otherwise(F.col("budget")))
        .withColumn("revenue",
                    F.when(F.col("revenue")==0,  None).otherwise(F.col("revenue")))
        .withColumn("roi",
                    F.when(F.col("budget").isNotNull() & (F.col("budget")>0),
                           (F.col("revenue")-F.col("budget"))/F.col("budget")))
       )

# ────────────────────────── 4. grava fato ───────────────────────
(fact.write
     .mode("overwrite")
     .partitionBy("tempo_sk")
     .parquet(args['REFINED_FACT_PATH']))

job.commit()
