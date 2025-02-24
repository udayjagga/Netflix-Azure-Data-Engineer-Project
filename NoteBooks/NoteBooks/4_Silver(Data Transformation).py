# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Data Transformation

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# Reading master data (Netflix titles file) from bronze layer

df = spark.read.format("delta")\
    .option("header", True)\
    .option("inferSchema", True)\
    .load("abfss://bronze@dlnetflixproject.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

display(df)

# COMMAND ----------

    df = df.fillna({"duration_minutes":0, "duration_seasons":1})

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.withColumn("duration_minutes", col("duration_minutes").cast(IntegerType()))
df = df.withColumn("duration_seasons", col("duration_seasons").cast(IntegerType()))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn("shorttitle", split(col('title'),':')[0])
df.display()

# COMMAND ----------

df = df.withColumn("rating", split(col("rating"),'-')[0])
df.display()

# COMMAND ----------

df = df.withColumn("type_flag", when(col('type')=='Movie',1)\
    .when(col('type')=='TV show',2).otherwise(0) )

df.display()

# COMMAND ----------

# Ranking the rows accoding to duration minutes

from pyspark.sql.window import Window

# COMMAND ----------

df = df.withColumn("Duration_ranking",dense_rank().over(Window.orderBy(col("duration_minutes").desc())))

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### How to do Ranking in sql queries in spark
# MAGIC

# COMMAND ----------

df.createOrReplaceTempView("temp_view")  # df is converted into temporary view for using in sql

# COMMAND ----------

df = spark.sql("""
               select *,
               dense_rank() over (order by duration_minutes desc) as Duration_ranking
                from temp_view
               """)

# COMMAND ----------

df.display()

# COMMAND ----------

df_vis = df.groupBy("type").agg(count("*").alias("Total_cnt"))
df_vis.display()

# COMMAND ----------

 df.write.format("delta")\
     .mode("overwrite")\
            .option("path","abfss://silver@dlnetflixproject.dfs.core.windows.net/netflix_titles")\
                .save()

# COMMAND ----------

