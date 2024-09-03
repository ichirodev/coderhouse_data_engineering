from require.news_sync.extract import extract as _extract
from require.news_sync.transform import transform as _transform
from require.news_sync.load import load as _load
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

topic = "Cryptocurrency"

out_data_stg_json = "/out_files/stg_news.json"
out_data_csv = "/out_files/news.csv"

clean_results_table = True

# Define the DAG
with DAG(
    dag_id="news_sync",
    start_date=datetime(2024, 8, 22),
    schedule_interval="30 0 * * *",
    catchup=True,
) as dag:
    extract = PythonOperator(
        task_id="extract",
        python_callable=_extract,
        provide_context=True,
        op_kwargs={
            "query": topic,
            "date": '{{ yesterday_ds }}',
            "file_in": out_data_stg_json,
        }
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=_transform,
        provide_context=True,
        op_kwargs={
            "file_in": out_data_stg_json,
            "file_out": out_data_csv,
        }
    )

    load = PythonOperator(
        task_id="load",
        python_callable=_load,
        provide_context=True,
        op_kwargs={
            "file_out": out_data_csv,
            "truncate": clean_results_table,
        }
    )

extract >> transform >> load
