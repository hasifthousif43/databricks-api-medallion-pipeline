from pyspark.sql.functions import *

df = spark.readStream.format("delta") \
    .load("abfss://silver@akstorageadls.dfs.core.windows.net/api_data")

agg_df = df.groupBy(
    window(col("ingestion_time"), "5 minutes"),
    col("userId")
).count()

agg_df.writeStream \
    .format("delta") \
    .outputMode("complete") \
    .option("checkpointLocation", "abfss://checkpoints@akstorageadls.dfs.core.windows.net/gold") \
    .start("abfss://gold@akstorageadls.dfs.core.windows.net/api_summary")