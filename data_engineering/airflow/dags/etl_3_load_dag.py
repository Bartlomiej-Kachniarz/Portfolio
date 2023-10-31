import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

path_to_airflow = os.getcwd().rstrip("/dags")

with DAG(dag_id="etl_3_load_dag", schedule_interval=None, start_date=datetime(2023, 1, 1), catchup=False) as dag:
    load_task = BashOperator(
        task_id="load_task",
        bash_command=f'echo -e ".separator ","\n.import --skip 1 \
            {path_to_airflow}/lab/orchestrated/airflow-transformed-data.csv top_level_domains" | \
                sqlite3 {path_to_airflow}/lab/orchestrated/airflow-load-db.db',
        dag=dag,
    )
