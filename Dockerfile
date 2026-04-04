# FROM python:3-alpine
FROM apache/airflow:3.1.8-python3.11

USER root

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

USER airflow

COPY dags /opt/airflow/dags
COPY plugins /opt/airflow/plugins

# ENTRYPOINT ["python3", "app.py"]

