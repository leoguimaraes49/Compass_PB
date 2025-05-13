from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def main():
    spark = SparkSession.builder \
        .appName("LabSpark_Parte2") \
        .master("local[*]") \
        .getOrCreate()

    # -------------------
    # Etapa 1: leitura
    # -------------------
    df_nomes = spark.read.csv(
        "nomes_aleatorios.txt",
        header=False,     
        inferSchema=False # tudo como string
    ).toDF("nome")

    print("=== Etapa 1: primeiras 5 linhas ===")
    df_nomes.show(5, truncate=False)

    # -------------------
    # Etapa 2: renomear, schema e show
    # -------------------
    df_nomes = df_nomes.withColumnRenamed("nome", "Nomes")
    print("=== Etapa 2: schema e primeiras 10 linhas ===")
    df_nomes.printSchema()
    df_nomes.show(10, truncate=False)

    # -------------------
    # Etapa 3: coluna Escolaridade aleatória
    # -------------------
    escolas = ["Fundamental", "Medio", "Superior"]
    df_nomes = df_nomes.withColumn(
        "Escolaridade",
        F.element_at(
            F.array([F.lit(x) for x in escolas]),
            (F.floor(F.rand() * len(escolas)) + F.lit(1)).cast("int")
        )
    )
    print("=== Etapa 3: adicionar Escolaridade (5 linhas) ===")
    df_nomes.show(5, truncate=False)

    # -------------------
    # Etapa 4: coluna Pais aleatório
    # -------------------
    paises = [
        "Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","Guyana",
        "Paraguay","Peru","Suriname","Uruguay","Venezuela","French Guiana"
    ]
    df_nomes = df_nomes.withColumn(
        "Pais",
        F.element_at(
            F.array([F.lit(p) for p in paises]),
            (F.floor(F.rand() * len(paises)) + F.lit(1)).cast("int")
        )
    )
    print("=== Etapa 4: adicionar Pais (5 linhas) ===")
    df_nomes.show(5, truncate=False)

    # -------------------
    # Etapa 5: coluna AnoNascimento aleatório
    # -------------------
    df_nomes = df_nomes.withColumn(
        "AnoNascimento",
        (F.floor(F.rand() * (2010 - 1945 + 1)) + 1945).cast("int")
    )
    print("=== Etapa 5: adicionar AnoNascimento (5 linhas) ===")
    df_nomes.show(5, truncate=False)

    # Registra a view temporária para SQL
    df_nomes.createOrReplaceTempView("pessoas")

    # -------------------
    # Etapa 6: DataFrame API — nascidos neste século
    # -------------------
    print("=== Etapa 6: nascidos >=2001 (DF API) ===")
    df_select = df_nomes \
        .filter(F.col("AnoNascimento") >= 2001) \
        .select("Nomes")
    df_select.show(10, truncate=False)

    # -------------------
    # Etapa 7: Spark SQL — mesma consulta
    # -------------------
    print("=== Etapa 7: nascidos >=2001 (SQL) ===")
    spark.sql(
        "SELECT Nomes FROM pessoas WHERE AnoNascimento >= 2001"
    ).show(10, truncate=False)

    # -------------------
    # Etapa 8: contar Millennials (1980–1994) via DataFrame API
    # -------------------
    qtde_millennials = df_nomes \
        .filter((F.col("AnoNascimento") >= 1980) & (F.col("AnoNascimento") <= 1994)) \
        .count()
    print(f"=== Etapa 8: total de Millennials (DF API): {qtde_millennials} ===")

    # -------------------
    # Etapa 9: contar Millennials via Spark SQL
    # -------------------
    print("=== Etapa 9: total de Millennials (SQL) ===")
    spark.sql("""
        SELECT COUNT(*) AS qtde_millennials
        FROM pessoas
        WHERE AnoNascimento BETWEEN 1980 AND 1994
    """).show()

    # -------------------
    # Etapa 10: agregação por País e Geração via SQL
    # -------------------
    print("=== Etapa 10: quantidade por País e Geração ===")
    resultado = spark.sql("""
      SELECT
        Pais,
        CASE
          WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
          WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
          WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
          WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
          ELSE 'Outra'
        END AS Geracao,
        COUNT(*) AS Quantidade
      FROM pessoas
      GROUP BY Pais, Geracao
      ORDER BY Pais ASC, Geracao ASC, Quantidade ASC
    """)
    resultado.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()
