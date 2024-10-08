import redshift_connector
import pandas as pd
import os


def load(file_out, truncate):
    rs_username = os.getenv("REDSHIFT_USER")
    rs_password = os.getenv("REDSHIFT_PASSWORD")
    rs_database = os.getenv("REDSHIFT_DATABASE")
    rs_host = os.getenv("REDSHIFT_URL")
    rs_port = os.getenv("REDSHIFT_PORT")

    connection = redshift_connector.connect(
        host=rs_host,
        port=rs_port,
        database=rs_database,
        user=rs_username,
        password=rs_password
    )

    cursor = connection.cursor()

    table = "news"

    df = pd.read_csv(file_out)

    columns = ', '.join(df.columns)
    data = ', '.join(["%s"] * len(df.columns))

    insert_query = f"INSERT INTO {table} ({columns}) VALUES ({data})"

    try:
        if truncate:
            cursor.execute("TRUNCATE TABLE news")

        for index, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))
        connection.commit()
        print("Load: Success!")
    except Exception as e:
        print(f"Failed to insert data: {e}")
        connection.rollback()

    cursor.close()

    connection.close()
