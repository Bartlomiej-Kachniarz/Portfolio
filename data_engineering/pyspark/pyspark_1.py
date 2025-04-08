import pandas as pd
from pyspark import SparkConf
from pyspark.sql import SparkSession

spark_config = (
    SparkConf()
    .setAppName("Bartlomiej Kachniarz's OOP App for Portfolio")
    .setMaster("local")
    .set("spark.executors.instances", 3)
    .set("spark.executors.cores", 5)
    .set("spark.memory.fraction", "0.5")
    .set("spark.executor.memory", "2g")
)


class SparkSessionManager:
    def __init__(self):
        self.spark = None

    def start_session(self, conf):
        self.spark = SparkSession.builder.config(conf=conf).getOrCreate()
        print("Started Spark Session...")

    def stop_session(self):
        if self.spark is not None:
            self.spark.stop()
            print("Stopped Spark Session.")


class Preprocessing:
    def __init__(self, df: list) -> None:
        self.df = df

    def transform(self, df):
        pass


class Preprocessing6:
    def __init__(self, df: list) -> None:
        self.df = df

    def transform(self, df):
        pass


class Preprocessing1(Preprocessing):

    def transform(self, df):
        try:
            df = df.dropna()
        except ValueError:
            return self.df
        except IndexError:
            return self.df
        self.df = df.filter(self.df["age"] > 35)

        return self.df
