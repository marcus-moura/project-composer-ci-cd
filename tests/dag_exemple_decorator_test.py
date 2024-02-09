import pytest

from airflow.models import DagBag
from airflow.utils.dag_cycle_tester import check_cycle

@pytest.fixture()
def dagbag():
    return DagBag(include_examples=False)


def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="dag_exemple_decorator")
    check_cycle(dag)