from airflow import DAG
from datetime import timedelta
from airflow.utils.timezone import pendulum
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

with DAG('dag_exemple',
         schedule="@once",
         catchup=False, 
         default_args=default_args, 
         tags=['exemplo2', 'learning', 'ci/cd'],
) as dag:
    init = EmptyOperator(task_id='start')
    
    with TaskGroup(group_id='group1') as group1:

        task1 = EmptyOperator(task_id='task1')
        task2 = EmptyOperator(task_id='task2')

        task1 >> task2
            
    finish = EmptyOperator(task_id='finish')

    init >> group1 >> finish