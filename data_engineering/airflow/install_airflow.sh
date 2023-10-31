#!/bin/bash
export AIRFLOW_HOME="/Users/Bartek/Desktop/Bartek/Programowanie/Python/Portfolio/data_engineering/airflow"

AIRFLOW_VERSION=2.7.2
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
echo "Installing Airflow Version $AIRFLOW_VERSION, with Python $PYTHON_VERSION"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow[celery,async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

airflow db reset -y
airflow db migrate
sed -i -e '/load_examples =/ s/= .*/= False/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/dag_dir_list_interval =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_batch_size =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_interval =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/workers =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg

airflow users delete -u admin
airflow users create --username admin --firstname Bartlomiej --lastname Kachniarz --role Admin --email bartlomiej.kachniarz01@gmail.com --password password159

cat ${AIRFLOW_HOME}/airflow-webserver.pid | xargs kill
cat ${AIRFLOW_HOME}/airflow-scheduler.pid | xargs kill

echo "" > ${AIRFLOW_HOME}/airflow-webserver.pid
echo "" > ${AIRFLOW_HOME}/airflow-scheduler.pid

airflow webserver -D
airflow scheduler -D