"""Dag doing two tasks"""

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
    dag_id="two_task_dag",
    description="Basic DAG implementation with two tasks.",
    schedule_interval=None,
    default_args=default_args,
) as dag:
    task_1 = BashOperator(task_id="first_bash_task", bash_command='echo "Running first of two tasks."')

    task_2 = BashOperator(
        task_id="second_bash_task",
        bash_command='echo "Sleeping for 3 seconds." && sleep 3 && echo "Running second of two tasks."',
    )

    task_1 >> task_2
