import json
from pyspark.sql.functions import current_timestamp
from src.api_client import fetch_api_data

# Load config
config = json.loads(dbutils.fs.head("/FileStore/configs/config.json"))

# Fetch API data
data = fetch_api_data(config["api_url"])

df = spark.createDataFrame(data)

df = df.withColumn("ingestion_time", current_timestamp())

# Write to Bronze
df.write.format("delta") \
  .mode("append") \
  .save("abfss://bronze@akstorageadls.dfs.core.windows.net/api_data")