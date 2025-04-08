import os

import pyspark.sql.functions as F
from pyspark.sql import SparkSession, Window

spark = SparkSession.builder.appName("Python Spark SQL").config("spark.driver.extraClassPath", "<path>").getOrCreate()

log_file = "/opt/homebrew/Cellar/apache-spark/3.5.2/README.md"
log_data = spark.read.text(log_file).cache()

current_dir = os.path.dirname(__file__)
df = (
    spark.read.csv(current_dir + "/Exercise Files/datasets/reported-crimes.csv", header=True)
    .withColumn("Date", F.to_timestamp(F.col("Date"), "MM/dd/yyyy hh:mm:ss a"))
    .filter(F.col("Date") <= F.lit("2018-11-11"))
)

# Column rename and cast with SQL
df_a = df.selectExpr([f"{c}::int as {c}_abc" for c in df.columns])

# Column rename and cast with native spark
for c in df.columns:
    df = df.withColumn(f"{c}_abc", F.col(c).cast("int")).drop(c)

# Window functions with SQL
df.withColumn("running_total", F.expr("sum(value) over (order by id rows between unbounded preceding and current row)"))

# Window functions with native spark
windowSpec = Window.orderBy("id").rowsBetween(Window.unboundedPreceding, Window.currentRow)

df_with_running_total_native = df.withColumn("running_total", F.sum("value").over(windowSpec))

# Read all parquet files in the directory (and subdirectories)
df_d = spark.read.load("var.parquet", format="parquet", pathGlobFilter="*.parquet")
