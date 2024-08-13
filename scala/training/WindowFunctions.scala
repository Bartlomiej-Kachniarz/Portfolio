/* Window Functions in Scala*/

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import spark.implicits._

val spark = SparkSession.builder()
    .master("local[4]")
    .appName("Window Functions App")
    .config("spark.driver.memory", "2g")
    .getOrCreate()

val turk_df = Seq(
    (1001, "Satılmış", "İdari", 4000),
    (1002, "Özge", "Personel", 3000),
    (1003, "Hüsnü", "Bilgi Sistemleri", 4000),
    (1004, "Menşure", "Muhasebe", 6500),
    (1005, "Doruk", "Personel", 3000),
    (1006, "Şilan", "Muhasebe", 5000),
    (1007, "Baran", "Personel", 7000),
    (1008, "Ülkü", "İdari", 4000),
    (1009, "Cüneyt", "Bilgi Sistemleri", 6500),
    (1010, "Gülşen", "Bilgi Sistemleri", 7000),
    (1011, "Melih", "Bilgi Sistemleri", 8000),
    (1012, "Gülbahar", "Bilgi Sistemleri", 10000),
    (1013, "Tuna", "İdari", 2000),
    (1014, "Raşel", "Personel", 3000),
    (1015, "Şahabettin", "Bilgi Sistemleri", 4500),
    (1016, "Elmas", "Muhasebe", 6500),
    (1017, "Ahmet Hamdi", "Personel", 3500),
    (1018, "Leyla", "Muhasebe", 5500),
    (1019, "Cuma", "Personel", 8000),
    (1020, "Yelda", "İdari", 5000),
    (1021, "Rojda", "Bilgi Sistemleri", 6000),
    (1022, "İbrahim", "Bilgi Sistemleri", 8000),
    (1023, "Davut", "Bilgi Sistemleri", 8000),
    (1024, "Arzu", "Bilgi Sistemleri", 11000)
).toDF("id", "name", "dept", "salary")

val tmp_view = turk_df.createOrReplaceTempView("Employees")

val dsWindow = Window
    .partitionBy("dept")
    .orderBy("salary")

val fiveWindows = turk_df
    .withColumn("rn", row_number().over(dsWindow))
    .withColumn("rank", rank().over(dsWindow))
    .withColumn("dense_rank", dense_rank().over(dsWindow))
    .withColumn("percent_rank", percent_rank().over(dsWindow))
    .withColumn("ntile", ntile(3).over(dsWindow))
    .show()

val fiveWindowsB = spark.sql("""
    |SELECT a.*,
    |ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary) as rn,
    |RANK() OVER(PARTITION BY dept ORDER BY salary) as rank,
    |DENSE_RANK() OVER(PARTITION BY dept ORDER BY salary) as dense_rank,
    |PERCENT_RANK() OVER(PARTITION BY dept ORDER BY salary) as percent_rank,
    |NTILE(3) OVER(PARTITION BY dept ORDER BY salary) as ntile
    |FROM Employees a
    |""".stripMargin)
    .show(false)


val fwdBwd = turk_df
    .withColumn("fill_forward", last($"temperature", ignoreNulls = true).over(wForward))
    .withColumn("fill_both", first("fill_forward", ignoreNulls = true).over(wBackWard))
    .show()


val textFile = sparkContext
    .textFile("")
    .flatMap(line => line.split(" "))
    .map(word => (word, 1))
    .reduceByKey(_ + _)