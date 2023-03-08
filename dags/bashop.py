import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'kbs111',
    'depends_on_past': False,
    'start_date': pendulum.datetime(2023, 2, 20, 19, 57),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}
with DAG(
    description = 'radio_record',
    default_args = default_args,
    dag_id = 'radio',
    schedule = None,#timedelta(days=1),
    tags = ["radio"],
) as dag:
    run = BashOperator(
        task_id = "pythonscript",
        bash_command = "python ~/airflow/dags/scripts/radio.py",
    )
    run


if __name__ == "__main__":
    dag.test()
