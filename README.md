# airflow

We are not using Dockerfile as of right now.

## Folder Structure Details
 /dags
     All DAGs files - the files corresponding to your data.
    
 /include
    All files we use in Data pipeline, e.g. Python Script, SQL requests, Bash Script, 
    anything that is not data, but we use in our data pipelines.

 /plugins
    If wee want to customize airflow instance? we can do that by adding plugins here.

 /test
     To ensure our tasks and data pipeline works.
    
 .env
     To export environment variables that will be be accessible in Airflow instance.
     This file will be useful to configure airflow instance and/or to create connections and vairables
     that we can use in our data pipelines.

packages.txt
    Useful when we want to install OS packages, e.g. wget, git etc.

requirements.txt
    Useful when neded to install Python Packages.
    e.g. If we want to requests to an API from data pipelines and for that we need
         Python package requests
    

# ================Follow steps below to setup and start Airflow=========================

# 🚀 Setup Airflow with Docker Desktop


## [1] 📁 Create Working Directory


    mkdir airflow
    cd airflow

### [2] Download Airflow Docker Compose file
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'

### [3] Create require Folders
    mkdir dags logs plugins config

### [4] Create .env file
    cat > .env
      AIRFLOW_UID=50000

### [5] Initialize AirFlow
    docker compose up airflow-init

    👉 This initializes the metadata database and prepares the environment.
    👉 Airflow stores run history and task state in its metadata DB.
================DO BELOW STEPS DAILY===========
cd /C/PERSONAL/Study-Work/AirFlow/airflow

docker compose up airflow-init

### [6] Start Aiflow in Background
    docker compose up -d

### [7] Create 'admin' user

docker compose exec airflow-apiserver airflow users create \
  --username admin \
  --password admin \
  --firstname Paresh \
  --lastname Patel \
  --role Admin \
  --email admin@example.com

### [8] Open Aurflow UI
  http://localhost:8080

### More Commands....

docker compose down
docker compose down -v
docker ps
docker compose restart
docker compose logs -f