#!/bin/bash
sudo kill $(sudo lsof -t -i:8000)
rm -rf /home/ubuntu/python_project/*
