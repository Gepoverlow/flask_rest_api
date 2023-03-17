FROM python:3.8-slim-buster
WORKDIR /pet_store
COPY requirements.txt  requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4" , "-b" , "0.0.0.0:8000" , "app:app"]
EXPOSE 8000