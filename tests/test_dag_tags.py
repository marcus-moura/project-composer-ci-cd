import os
import pytest
from airflow.models import DagBag

def get_dags():
    """
    Generate a tuple of dag_id, <DAG objects> in the DagBag
    """
    dag_bag = DagBag(include_examples=False)

    def strip_path_prefix(path):
        return os.path.relpath(path, os.environ.get("AIRFLOW_HOME"))

    return [(k, v, strip_path_prefix(v.fileloc)) for k, v in dag_bag.dags.items()]


@pytest.mark.parametrize(
    "dag_id,dag,fileloc", get_dags(), ids=[x[2] for x in get_dags()]
)
def test_dag_tags(dag_id, dag, fileloc):
    """
    test if a DAG is tagged
    """
    assert dag.tags, f"{dag_id} in {fileloc} has no tags"