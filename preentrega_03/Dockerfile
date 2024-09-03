# Start from a base image with Python 3.10
FROM python:3.10-slim

# Set environment variables for Airflow
ENV AIRFLOW_HOME=/usr/local/airflow
ENV AIRFLOW_VERSION=2.10.0
ENV PYTHON_VERSION=3.10
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Install Airflow
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" \
    --constraint "${CONSTRAINT_URL}"
# Install DAGs requirements
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the DAGs folder
COPY ./dags ${AIRFLOW_HOME}/dags

# Set up Airflow user credentials
ENV airflow_default_user=admin
ENV airflow_default_email=admin@admin.com
ENV airflow_default_password=administrador

# Init DB and set initial user
RUN airflow db init
RUN airflow users  create --role Admin --username "${airflow_default_user}" --email "${airflow_default_email}" --firstname Airflow --lastname Admin --password "${airflow_default_password}"

# Install supervisor
RUN apt-get update && apt-get install -y supervisor && apt-get clean

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the Airflow port
EXPOSE 8080

RUN mkdir out_files

CMD ["supervisord", "-n"]
