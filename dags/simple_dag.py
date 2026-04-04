from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract():
    print(" Extracting Data...")
    
def transform():
    print(" Transforming Data...")

def load():
    print(" Loading Data...")

def notify():
    print(" Sending Notifications...")

with DAG(
    dag_id="simple_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    description="My 1st Pipeline with multiple tasks...555"
) as dag:
    
    t1 = PythonOperator(
        task_id="extract",
        python_callback=extract
    )

    t2 = PythonOperator(
        task_id="transform",
        python_callback=transform
    )

    t3 = PythonOperator(
        task_id="load",
        python_callback=load
    )

    t4 = PythonOperator(
        task_id="notify",
        python_callback=notify
    )

    t1 >> t2 >> t3 >> t4