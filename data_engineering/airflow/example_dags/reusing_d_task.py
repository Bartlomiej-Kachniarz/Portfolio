from datetime import datetime

from airflow.decorators import dag, task


@task
def add_task(a, b):
    print(f"Task args: a={a}, b={b}")
    return a, b


@dag(start_date=datetime(2023, 1, 1))
def dag_1():
    start = add_task.override(task_id="start")(1, 2)
    for i in range(4):
        start >> add_task.override(task_id=f"add_start_{i}")(start, i)


@dag(start_date=datetime(2023, 1, 1))
def dag_2():
    start = add_task(1, 2)
    for i in range(5):
        start >> add_task.override(task_id=f"new_add_start_{i}")(start, i)


first_dag = dag_1()
second_dag = dag_2()
