from pyspark.sql.functions import *

df = spark.readStream.format("delta") \
    .load("abfss://bronze@akstorageadls.dfs.core.windows.net/api_data")

clean_df = df \
    .withWatermark("ingestion_time", "10 minutes") \
    .dropDuplicates(["id"])

query = clean_df.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "abfss://checkpoints@akstorageadls.dfs.core.windows.net/silver") \
    .start("abfss://silver@akstorageadls.dfs.core.windows.net/api_data")