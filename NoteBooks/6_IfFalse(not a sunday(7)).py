# Databricks notebook source
var = dbutils.jobs.taskValues.get(taskKey="WeekDayLookUp", key="weekoutput")

# COMMAND ----------

print(var)

# COMMAND ----------

