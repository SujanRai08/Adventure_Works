from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data():
    print("Extracting data...")

def transform_data():
    print("Transforming data...")

def load_data():
    print("Loading data...")

default_args = {
    "start_date": datetime(2024, 2, 1),
    "schedule_interval": "@daily"
}

dag = DAG("etl_pipeline", default_args=default_args)

task1 = PythonOperator(task_id="extract", python_callable=extract_data, dag=dag)
task2 = PythonOperator(task_id="transform", python_callable=transform_data, dag=dag)
task3 = PythonOperator(task_id="load", python_callable=load_data, dag=dag)

task1 >> task2 >> task3


# Data pipelines need automation to run scheduled ETL jobs. 
#  Use case: Scheduling and automating ETL pipelines.