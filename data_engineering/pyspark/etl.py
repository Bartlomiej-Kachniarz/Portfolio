import pyspark.sql as pysql

spark = (
    pysql.SparkSession.builder.appName("Python Spark SQL").config("spark.driver.extraClassPath", "<path>").getOrCreate()
)
