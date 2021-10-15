# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

#INSTALL GIT
RUN apt-get -y update
RUN apt-get -y install git

#Clone the two repos
#RUN git clone https://${USERNAME}:${PASSWORD}@github.com/${USERNAME}/COVID19-Dataset-Netherlands.git
RUN git clone https://${USERNAME}:${PASSWORD}@github.com/${USERNAME}/COVID19-Dataset-Netherlands.git
RUN git clone https://github.com/${USERNAME}/COVID19-Dataset-Downloader.git

#run the script
RUN python ./COVID19-Dataset-Downloader/src/covid_data_downloader.py

WORKDIR /app/COVID19-Dataset-Netherlands

RUN git add .
RUN git commit -m "scripted update"
RUN git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/${USERNAME}/COVID19-Dataset-Netherlands.git
RUN git push -u origin main


