from airflow.decorators import dag, task
from datetime import timedelta
# from airflow.utils.timezone import pendulum
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator

local_tz = pendulum.timezone("America/Sao_Paulo")

default_args = {
    'owner': "Learning",
    'start_date': pendulum.today("America/Sao_Paulo").add(days=-1),
    'retries': 1,
    'depends_on_past': False,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id="dag_exemple_decorator",
    schedule="@once",
    catchup=False, 
    default_args=default_args, 
    tags=['decorator']
)
def dag_exemplo_decorator():

    init = EmptyOperator(task_id='start')

    @task
    def task1():
        print("task1")

    finish = EmptyOperator(task_id='finish')

    init >> task1() >> finish
    
dag_exemplo_decorator()
