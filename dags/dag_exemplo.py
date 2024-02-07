import airflow
from datetime import timedelta
from airflow.decorators import dag
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': "Learning",
    'start_date': airflow.utils.dates.days_ago(1),
    'retries': 1,
    'depends_on_past': False,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id="dag_exemplo",
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=['exemplo', 'learning', 'ci/cd'],
)
def workflow():

    init = EmptyOperator(task_id='start')
    
    with TaskGroup(group_id='group1') as group1:

        task1 = EmptyOperator(task_id='task1')
        task2 = EmptyOperator(task_id='task2')

        task1 >> task2
            
    finish = EmptyOperator(task_id='finish')

    init >> group1 >> finish

workflow()