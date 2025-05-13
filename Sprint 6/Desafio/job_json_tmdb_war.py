import sys, re
from awsglue.utils import getResolvedOptions
from pyspark.sql import SparkSession, functions as F
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv,
    ['JOB_NAME', 'RAW_JSON_PATH', 'TRUSTED_JSON_PATH'])

spark = SparkSession.builder.getOrCreate()
glueContext = GlueContext(spark.sparkContext)
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

#Lê todos os JSONs da RAW
df = (spark.read
      .option("recursiveFileLookup", "true") 
      .json(args['RAW_JSON_PATH']))

# Extrai ano/mes/dia do path do arquivo
df = (df
      .withColumn("ano", F.regexp_extract(F.input_file_name(), r'/(\d{4})/', 1))
      .withColumn("mes", F.regexp_extract(F.input_file_name(), r'/\d{4}/(\d{2})/', 1))
      .withColumn("dia", F.regexp_extract(F.input_file_name(), r'/\d{4}/\d{2}/(\d{2})/', 1)))

# Salva em Parquet particionado
(df.write
    .mode("overwrite")
    .partitionBy("ano", "mes", "dia")
    .parquet(args['TRUSTED_JSON_PATH']))

job.commit()