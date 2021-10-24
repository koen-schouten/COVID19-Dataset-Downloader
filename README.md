# COVID19 Dataset Downloader

COVID19-Dataset-Downloader is used to daily download COVID data from the [RIVM COVID-19 dataset](https://data.rivm.nl/covid-19/).

To run copy the dockerfile and execute the following commands:


>docker build --build-arg USERNAME=\<username> --build-arg PASSWORD=\<github-key> --build-arg EMAIL=\<email> -t covid-downloader .
  
>docker run -i -d covid-downloader

# Note:

**Password is not hidden**. Only run on a system that's completely controlled by yourself.

To run this yourself make sure a github.com/{USERNAME}/COVID19-Dataset-Netherlands.git repo exists.
