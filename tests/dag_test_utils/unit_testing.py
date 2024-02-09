from airflow.models.dag import DAG
from typing import Callable
from airflow.decorators import dag
from airflow.utils.dag_cycle_tester import check_cycle

def assert_has_valid_dag(module):
    """Assert that a module contains a valid DAG."""
    no_dag_found = True

    # Verifica cada objeto no módulo
    for obj in vars(module).values():
        # Verifica se o objeto é uma DAG definida usando a classe models.DAG
        if isinstance(obj, DAG):
            no_dag_found = False
            check_cycle(obj)  # Throws if a task cycle is found.
        # Verifica se o objeto é uma DAG definida usando o decorador @dag
        else:
            no_dag_found = False
            check_cycle(obj)  # Throws if a task cycle is found.

    if no_dag_found:
        raise AssertionError("module does not contain a valid DAG")