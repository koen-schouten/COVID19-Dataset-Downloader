# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app

ARG EMAIL
ARG USERNAME
ARG PASSWORD

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

RUN  git config --global user.email ${EMAIL}
RUN  git config --global user.name ${USERNAME}

RUN git add .
RUN git commit -m "scripted update"; exit 0
RUN git remote set-url origin https://${USERNAME}:${PASSWORD}@github.com/${USERNAME}/COVID19-Dataset-Netherlands.git
RUN git push -u origin main; exit 0


#install crontab

# Add crontab file in the cron directory
RUN mkdir /etc/cron.d/
RUN cp -R /app/COVID19-Dataset-Downloader/crontab /etc/cron.d/repeatscript-cron
# Give execution rights on the cron repeat script
RUN chmod +x /app/COVID19-Dataset-Downloader/repeatscript.sh

# Give execution rights for the cron tab
RUN chmod 0644 /etc/cron.d/repeatscript-cron

#install cron
RUN apt-get -y install cron

#run crontab command to make sure the file is loaded in crontab
RUN crontab /etc/cron.d/repeatscript-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log
# Run the command on container startup
CMD cron && tail -f /var/log/cron.log