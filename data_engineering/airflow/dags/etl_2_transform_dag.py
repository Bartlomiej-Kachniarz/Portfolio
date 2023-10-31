import os
from datetime import date, datetime

import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

path_to_airflow_dir = os.getcwd().rstrip("/dags")

with DAG(dag_id="etl_2_transform_dag", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:

    def transform_data():
        """Reads csv file and writes it after transformation."""
        today = date.today()
        df = pd.read_csv(f"{path_to_airflow_dir}/lab/orchestrated/airflow-extracted-data.csv")
        generic_type_df = df[df["Type"] == "generic"]
        generic_type_df["Date"] = today.strftime("%Y-%m-%d")
        generic_type_df.to_csv(f"{path_to_airflow_dir}/lab/orchestrated/airflow-transformed-data.csv", index=False)

    transform_task = PythonOperator(task_id="transform_task", python_callable=transform_data, dag=dag)
