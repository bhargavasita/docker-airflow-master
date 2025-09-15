from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
import pandas as pd

def filter1():
    df=pd.read_csv("/usr/local/docker-airflow-master/input/UniversalBank.csv");
    print(df[df['ID']<20]);
with DAG(
    dag_id="Filtering_DAG",
    start_date=datetime(year=2025,month=9,day=15),
    schedule_interval="@daily",

)as DAG:
    #task1
    Filter_CSV=PythonOperator(
        task_id="Flitering_Data",
        python_callable=filter1,
    )