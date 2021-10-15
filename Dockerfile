# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

#INSTALL GIT
RUN apt-get -y update
RUN apt-get -y install git

#DEFINE PASSWORD And username for git
ARG PASSWORD=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
ARG USERNAME=koen-schouten
ARG USEREMAIL=schouten_koen@hotmail.com

#Clone the two repos
RUN git clone https://github.com/koen-schouten/COVID19-Dataset-Netherlands.git
RUN git clone https://github.com/koen-schouten/COVID19-Dataset-Downloader.git


#run the script
RUN python ./COVID19-Dataset-Downloader/src/covid_data_downloader.py
CMD ["python", "./COVID19-Dataset-Downloader/src/covid_data_downloader.py"]

WORKDIR /app/COVID19-Dataset-Netherlands

RUN git config --global user.email $USEREMAIL
RUN git config --global user.name $USERNAME

RUN git commit -m "scripted update"
RUN git remote add origin 'httpa://github.com/koen-schouten/COVID19-Dataset-Netherlands.git'
RUN git push -u origin master