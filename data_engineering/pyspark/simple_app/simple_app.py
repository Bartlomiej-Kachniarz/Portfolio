from pyspark.sql import SparkSession

log_file = "/opt/homebrew/Cellar/apache-spark/3.5.1/README.md"
spark = SparkSession.builder.appName("Simple Application").getOrCreate()
log_data = spark.read.text(log_file).cache()

num_a = log_data.filter(log_data.value.contains("a")).count()
num_b = log_data.filter(log_data.value.contains("b")).count()

print(f"Lines with a: {num_a}, Lines with b: {num_b}")

spark.stop()
