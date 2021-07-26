FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY ./database/seed/books_50.csv books_50.csv

CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]