from airflow import DAG
# from airflow.operators.python import PythonOperator
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import time

def task_1():
    print("Task 1 running")

def task_2():
    print("Task 2 running")

def task_3():
    print("Task 3 running")

def long_task():
    print("Starting Long Task......")
    time.sleep(6000)
    print(" Long Task is completed.")

with DAG(
    dag_id="simple_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["test", "demo", "paresh"]
) as dag:

    t1 = PythonOperator(
        task_id="task_1",
        python_callable=task_1
    )

    t2 = PythonOperator(
        task_id="task_2",
        python_callable=task_2
    )

    t3 = PythonOperator(
        task_id="task_3",
        python_callable=task_3
    )

    t1 >> t2 >> t3
