from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataProcessing").getOrCreate()

# Load CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Transformation
df_filtered = df.filter(df["Column"] > 100)

# Show Data
df_filtered.show()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('ExampleApp').getOrCreate()
data = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
df = spark.createDataFrame(data, ['Name', 'Age'])

df_filtered = df.filter(df.Age > 28)
df_filtered.show()
