# Databricks notebook source
# MAGIC %md
# MAGIC # Silver NoteBook Lookup Tables

# COMMAND ----------

# MAGIC %md
# MAGIC # Parameters

# COMMAND ----------

# This code will create a parameters like sourcefolder and targetfolder through which we can load no of files with just sending the names of the files in these paramenters

dbutils.widgets.text("sourcefolder", "netflix_directors")    #netflix_directors is default values
dbutils.widgets.text("targetfolder", "netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC # Variables

# COMMAND ----------

# we are storing the parameters values in these variables
var_src_folder = dbutils.widgets.get("sourcefolder")
var_trg_folder = dbutils.widgets.get("targetfolder")

# COMMAND ----------

print(var_src_folder, var_trg_folder)

# COMMAND ----------

df = spark.read.format("csv")\
    .option("header", True)\
    .option("inferScheman", True)\
    .load(f"abfss://bronze@dlnetflixproject.dfs.core.windows.net/{var_src_folder}")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("path",f"abfss://silver@dlnetflixproject.dfs.core.windows.net/{var_trg_folder}")\
    .save()

# COMMAND ----------

