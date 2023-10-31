"""Dag doing only one task"""
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "Bart",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "catchup": False,
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="one_task_dag",
    description="Basic DAG implementation with only one task.",
    schedule_interval=None,
    default_args=default_args,
) as dag:
    task_1 = BashOperator(
        task_id="one_and_only_task", bash_command='echo "Hello World!" > /tmp/hello-world.txt', dag=dag
    )
