FROM python:3.6.5
ADD . /app
WORKDIR /app

RUN apt-get update
# Install GDAL dependencies
RUN apt-get install -y libgdal-dev gdal-bin g++ --no-install-recommends && \
    apt-get clean -y
RUN export CPLUS_INCLUDE_PATH=/usr/include/gdal
RUN export C_INCLUDE_PATH=/usr/include/gdal
RUN pip install GDAL
RUN pip install -r ./requirements.txt
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]