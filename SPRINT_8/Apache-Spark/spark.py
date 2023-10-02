from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, when

spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

df_nomes = spark.read.csv(r"C:\Users\Usuario\Desktop\EstagioCompassRepo\SPRINT_8\nomes_aleatorios.txt")

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes").withColumnRenamed("_c1", "Data de Nascimento")

df_nomes = df_nomes.withColumn("random", expr("floor(rand() * 3) + 1"))
df_nomes = df_nomes.withColumn("Escolaridade", when(col("random") == 1, "Fundamental")
                                .when(col("random") == 2, "Medio")
                                .otherwise("Superior"))

df_nomes = df_nomes.withColumn("random", expr("floor(rand() * 13) + 1"))
df_nomes = df_nomes.withColumn("Pais", when(col("random") == 1, "Argentina")
                                    .when(col("random") == 2, "Bolívia")
                                    .when(col("random") == 3, "Chile")
                                    .when(col("random") == 4, "Colômbia")
                                    .when(col("random") == 5, "Equador")
                                    .when(col("random") == 6, "Guiana")
                                    .when(col("random") == 7, "Paraguai")
                                    .when(col("random") == 8, "Peru")
                                    .when(col("random") == 9, "Suriname")
                                    .when(col("random") == 10, "Uruguai")
                                    .when(col("random") == 11, "Venezuela")
                                    .when(col("random") == 12, "Paraguai")
                                    .when(col("random") == 13, "Suriname"))

df_nomes = df_nomes.drop("random")
df_nomes = df_nomes.withColumn("AnoNascimento", expr(f"floor(rand() * (2011 - 1945) + 1945)"))

df_nomes.show(10)

df_nomes_seculo = df_nomes.select("Nomes", "AnoNascimento").filter(col("AnoNascimento") >= 2001)
df_nomes_seculo.show(15)


df_nomes.createOrReplaceTempView("pessoas")
spark.sql("select * from pessoas").show(5)

millenials_filtrados = df_nomes.filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1999))
millenials_quantidade= millenials_filtrados.count()
print(f'Quantidade de nascidos entre 1980 e 1999: {millenials_quantidade}')

spark.sql("select count(*) as Millenials from pessoas where AnoNascimento between 1980 and 1999").show()

sSQL_query = """
                SELECT Pais, 
                Geracoes,
                COUNT(*) AS Quantidade
                FROM (
                    SELECT Pais,
                        CASE 
                            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
                            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
                            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
                            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
                            ELSE 'Outros'
                        END AS Geracoes
                    FROM pessoas
                ) AS subquery
                GROUP BY Pais, Geracoes
                ORDER BY Pais, Geracoes
            """

df_novo_quantidade_pais = spark.sql(sSQL_query)
df_novo_quantidade_pais.show()