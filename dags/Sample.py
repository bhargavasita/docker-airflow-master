from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator


def val_check():
    print("running validation check")
with DAG(
    dag_id="First_DAG",
    start_date=datetime(year=2025,month=9,day=15),
    schedule_interval="@daily",
    
)as DAG:
    #task1
    Validation_check=PythonOperator(
        task_id="Val_check",
        python_callable=val_check,
    )

