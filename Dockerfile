FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT ["python3", "app.py"]