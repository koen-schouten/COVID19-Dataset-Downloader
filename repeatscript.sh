#!/bin/bash

#change to the dataset dir
cd /app/COVID19-Dataset-Netherlands

#pull main from orgin
git pull origin main

cd /app
#run the python script
/usr/local/bin/python /app/COVID19-Dataset-Downloader/src/covid_data_downloader.py

#change to the dataset dir
cd /app/COVID19-Dataset-Netherlands

#commit the changes made by the python script
git add .
git commit -m "scripted update"

#push the update to github
git push -u origin main