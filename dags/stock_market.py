from airflow.decorators import dag
from datetime import datetime

@dag(
    start_date=datetime(2024, 01, 01),
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
)

def stock_market():
    pass

stock_market()