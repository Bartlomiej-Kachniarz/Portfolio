from datetime import datetime

from airflow.decorators import dag
from reusing_d_task import add_task


@dag(start_date=datetime(2023, 1, 1))
def use_add_task():
    start = add_task.override(priority_weight=2)(1, 2)
    for i in range(3):
        start >> add_task.override(task_id=f"reused_add_task_{i}")(start, i)


recycling_dag = use_add_task()
