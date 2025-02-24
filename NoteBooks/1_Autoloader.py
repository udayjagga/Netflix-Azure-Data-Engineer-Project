# Databricks notebook source
# MAGIC %md
# MAGIC # Incremental Data loading using AutoLoader

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA netflix_catalog.net_schema

# COMMAND ----------

# Creating checkpoint in silver container for data reading reading check points
checkpoint_path = "abfss://silver@dlnetflixproject.dfs.core.windows.net/checkpoint"

# COMMAND ----------

# Reading the stream data from raw from DL
df = spark.readStream\
  .format("cloudFiles")\
  .option("cloudFiles.format", "csv")\
  .option("cloudFiles.schemaLocation", checkpoint_path)\
  .load("abfss://raw@dlnetflixproject.dfs.core.windows.net")

# COMMAND ----------

display(df)

# COMMAND ----------

# Now write the stream data to the bronze container which we loaded using above code (raw floder in DL to broze folder in DL netflix titles data)
df.writeStream\
  .option("checkpointLocation", checkpoint_path)\
  .trigger(processingTime='10 seconds')\
  .start("abfss://bronze@dlnetflixproject.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

