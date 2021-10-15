# COVID19 Dataset Downloader

COVID19-Dataset-Downloader is used to daily download COVID data from the [RIVM COVID-19 dataset](https://data.rivm.nl/covid-19/).

To run copy the dockerfile and execute the following commands:


>docker build --build-arg USERNAME=<username> --build-arg PASSWORD=<password> --build-arg EMAIL=<email> -t covid-downloader-test .
  
>docker run -i -d covid-downloader-test
