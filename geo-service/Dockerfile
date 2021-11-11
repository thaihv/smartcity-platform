FROM python:3.6.5
ADD . /app
WORKDIR /app
RUN pip install flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app"]