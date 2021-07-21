FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 5000

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD ["python", "-m" , "flask", "run", "--host=0.0.0.0"]