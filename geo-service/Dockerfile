FROM python:3.6.5
ADD . /app
WORKDIR /app
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
ARG CPLUS_INCLUDE_PATH=/usr/include/gdal
ARG C_INCLUDE_PATH=/usr/include/gdal    
RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]