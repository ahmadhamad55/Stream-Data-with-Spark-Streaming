from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr, count, avg
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("CSV Stream").getOrCreate()

schema = StructType([
    StructField("id", IntegerType()),
    StructField("first_name", StringType()),
    StructField("last_name", StringType()),
    StructField("age", IntegerType()),
    StructField("salary", DoubleType()),
    StructField("gender", StringType())
])

streamingDF = spark \
    .readStream \
    .option("header", "true") \
    .schema(schema) \
    .csv("/user/zaka/emp_data_files/*.csv")

aggDF = streamingDF \
    .groupBy("gender") \
    .agg(avg("salary").alias("avg_salary"), count("gender").alias("count")) \
    .orderBy("gender")

query = aggDF.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
