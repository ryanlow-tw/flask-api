FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./database/seed/books_50.csv books_50.csv

CMD python ./database/seed/seed_docker_postgres.py

CMD python app.py

