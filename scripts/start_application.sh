#!/bin/bash

CURRENT_IP=`ifconfig | grep inet | head -1 | awk '{ print $2 }' | awk -F':' '{ print $2 }'`
cd /home/ubuntu/python_project
source /home/ubuntu/python_project/venv/bin/activate
python /home/ubuntu/python_project/manage.py migrate
nohup python /home/ubuntu/python_project/manage.py runserver ${CURRENT_IP}:8000 > /dev/null 2>&1 &


