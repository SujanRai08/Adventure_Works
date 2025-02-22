from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)
df = df.withColumn("new_price", df["price"] * 1.1)
df.show()


# Pandas can't handle terabytes of data, but PySpark can.👉 Use case: Big Data processing, large-scale analytics.