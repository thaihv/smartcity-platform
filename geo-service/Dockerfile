FROM hakonamdal/python-gdal:python3.8-gdal3.1.2
RUN pip install gdal==3.1.2
ADD . /app
WORKDIR /app
RUN pip install -r ./requirements.txt
EXPOSE 5000
ENV FLASK_ENV=production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]