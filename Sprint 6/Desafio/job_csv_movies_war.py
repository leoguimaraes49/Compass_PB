import sys
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession, functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv,
    ['JOB_NAME', 'RAW_CSV_PATH', 'TRUSTED_CSV_PATH']
)

spark = SparkSession.builder.getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# 1) Lê todos os CSV separados por |
df = (spark.read
        .option("header", "true")
        .option("delimiter", "|")
        .option("recursiveFileLookup", "true")
        .csv(args['RAW_CSV_PATH']))

# 2) Mantém só filmes cujo campo "genero" contém 'War'
df_war = df.filter(F.col("genero").contains("War"))

# 3) Converte colunas numéricas
df_war = (df_war
          .withColumn("anoLancamento", F.col("anoLancamento").cast("int"))
          .withColumn("tempoMinutos", F.col("tempoMinutos").cast("int"))
          .withColumn("notaMedia",   F.col("notaMedia").cast("double"))
          .withColumn("numeroVotos", F.col("numeroVotos").cast("int")))

# 4) Adiciona colunas de partição (data de ingestão = hoje)
hoje = F.current_date()
df_war = (df_war
          .withColumn("ano", F.year(hoje))
          .withColumn("mes", F.date_format(hoje, "MM"))
          .withColumn("dia", F.date_format(hoje, "dd")))

# 5) Grava em Parquet particionado ano/mes/dia
(df_war.write
      .mode("overwrite")
      .partitionBy("ano", "mes", "dia")
      .parquet(args['TRUSTED_CSV_PATH']))

job.commit()
