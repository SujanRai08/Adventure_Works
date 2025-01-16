from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def extract():
    print('extracting the data ... ')

def transform():
    print('tranformation data..')

def load():
    print('loading....')

with DAG('etl_pipeline',start_date = datetime(2025,1,1),schedule_interval = '@daily') as dag:
    extract_task = PythonOperator(task_id='extract', python_callable=extract)
    transform_task = PythonOperator(task_id='transform', python_callable=transform)
    load_task = PythonOperator(task_id='load', python_callable=load)

    extract_task >> transform_task >> load_task