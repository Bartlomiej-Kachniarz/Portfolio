import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

path_to_airflow = os.getcwd().rstrip("/dags")

with DAG(dag_id="etl_1_extract_dag", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    extract_task = BashOperator(
        task_id="extract_task",
        bash_command=f"wget -c https://datahub.io/core/top-level-domain-names/r/top-level-domain-names.csv.csv -O \
        {path_to_airflow}/lab/orchestrated/airflow-extracted-data.csv",
    )
