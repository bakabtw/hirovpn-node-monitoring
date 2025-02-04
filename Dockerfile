FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    gcc

RUN ["pip", "install", "-r", "requirements.txt"]

RUN apt-get -y purge python3-dev gcc && \
    apt-get -y --purge autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python3", "app.py"]