#!/bin/bash
export AIRFLOW_HOME="/Users/Bartek/Desktop/Bartek/Programowanie/Python/Portfolio/data_engineering/airflow"

AIRFLOW_VERSION=2.5.1
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

if command -v airflow > /dev/null 2>&1
then
    echo 'Apache Airflow found. Version:' $AIRFLOW_VERSION 'at:' $AIRFLOW_HOME
else
    echo 'Installing Apache Airflow...'
    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
fi

airflow db reset -y
airflow db init
sed -i -e '/WTF_CSRF_ENABLED =/ s/= .*/= False/' ${AIRFLOW_HOME}/webserver_config.py
sed -i -e '/load_examples =/ s/= .*/= True/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/dag_dir_list_interval =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_batch_size =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/worker_refresh_interval =/ s/= .*/= 0/' ${AIRFLOW_HOME}/airflow.cfg
sed -i -e '/workers =/ s/= .*/= 2/' ${AIRFLOW_HOME}/airflow.cfg

# cat ${AIRFLOW_HOME}/airflow-webserver.pid | xargs kill
# cat ${AIRFLOW_HOME}/airflow-scheduler.pid | xargs kill

echo "" > ${AIRFLOW_HOME}/airflow-webserver.pid
echo "" > ${AIRFLOW_HOME}/airflow-scheduler.pid

airflow users delete -u admin
airflow users create --username admin --firstname Bartlomiej --lastname Kachniarz --role Admin --email bartlomiej.kachniarz01@gmail.com --password password159

airflow webserver -D
airflow scheduler -D
