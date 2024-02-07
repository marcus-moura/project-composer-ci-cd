import internal_unit_testing

def test_dag_import():
    from dags import dag_exemplo as module

    internal_unit_testing.assert_has_valid_dag(module)