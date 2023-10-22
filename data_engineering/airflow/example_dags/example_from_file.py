import pandas as pd
from airflow.decorators import task
from airflow.sensors.filesystem import FileSensor


@task()
def extract_from_file():
    """
    #### Extract from file task
    A simple Extract task to get data ready for the rest of the data
    pipeline, by reading the data from a file into a pandas dataframe
    """
    order_data_file = "/tmp/order_data.csv"
    pd.read_csv(order_data_file)


file_task = FileSensor(task_id="check_file", filepath="/tmp/order_data.csv")
order_data = extract_from_file()

file_task >> order_data
