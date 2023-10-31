"""Basic ETL DAG"""
import os
from datetime import date, datetime

import pandas as pd
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

path_to_airflow = os.getcwd().rstrip("/dags")

with DAG(dag_id="basic_etl_dag", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    extract_task = BashOperator(
        task_id="extract_task",
        bash_command=f"wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O \
        {path_to_airflow}/lab/orchestrated/airflow-extracted-data.csv",
    )

    def transform_data():
        """Reads csv file and writes it after transformation."""
        today = date.today()
        df = pd.read_csv(f"{path_to_airflow}/lab/orchestrated/airflow-extracted-data.csv")
        generic_type_df = df[df["Type"] == "generic"]
        generic_type_df["Date"] = today.strftime("%Y-%m-%d")
        generic_type_df.to_csv(f"{path_to_airflow}/lab/orchestrated/airflow-transformed-data.csv", index=False)

    transform_task = PythonOperator(task_id="transform_task", python_callable=transform_data)

    load_task = BashOperator(
        task_id="load_task",
        bash_command=f'echo -e ".separator ","\n.import --skip 1 \
            {path_to_airflow}/lab/orchestrated/airflow-transformed-data.csv top_level_domains" |\
                sqlite3 {path_to_airflow}/lab/orchestrated/airflow-load-db.db',
    )

    extract_task >> transform_task >> load_task
