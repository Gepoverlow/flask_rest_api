FROM python:3.8-slim-buster
WORKDIR /pet_store
COPY requirements.txt  requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "-b" , "0.0.0.0:8000", "--workers=1", "--worker-class=sync", "--preload", "app:app"]
EXPOSE 8000