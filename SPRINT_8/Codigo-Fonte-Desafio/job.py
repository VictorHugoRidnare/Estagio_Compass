import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue import DynamicFrame
from pyspark.sql.functions import col, round, to_date
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

df = glueContext.create_dynamic_frame_from_catalog(database='jsfilmes', table_name='fato_table').toDF()

df1 = df.select("data_de_lancamento")
df2 = df.select("titulo", "visão_geral")

df3 = df.withColumn("Porcentagem_lucro", round((col("receita") - col("orcamento")) / col("orcamento") * 100, 2))
df3 = df3.select("orcamento", "receita", "votos", "Porcentagem_lucro", "media_de_votos")

sink_table1 = glueContext.getSink(connection_type="s3", path="s3://movies-refined/Refined/data/",
    enableUpdateCatalog=True, updateBehavior="UPDATE_IN_DATABASE")
sink_table1.setFormat("parquet")
sink_table1.setCatalogInfo(catalogDatabase="jsfilmes", catalogTableName="dimensao_data")
sink_table1.writeFrame(df1)

sink_table2 = glueContext.getSink(connection_type="s3", path="s3://movies-refined/Refined/filme/",
    enableUpdateCatalog=True, updateBehavior="UPDATE_IN_DATABASE")
sink_table2.setFormat("parquet")
sink_table2.setCatalogInfo(catalogDatabase="jsfilmes", catalogTableName="dimensao_filme")
sink_table2.writeFrame(df2)

sink_table3 = glueContext.getSink(connection_type="s3", path="s3://movies-refined/Refined/fatos/",
    enableUpdateCatalog=True, updateBehavior="UPDATE_IN_DATABASE")
sink_table3.setFormat("parquet")
sink_table3.setCatalogInfo(catalogDatabase="jsfilmes", catalogTableName="fatos")
sink_table3.writeFrame(df3)

job.commit()