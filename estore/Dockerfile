# pull official base image
FROM python:3.11.4-slim-buster


# set work directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat apt-utils pkg-config libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*
# install dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade psycopg2-binary
COPY ./requirements.txt .
RUN pip install  --no-cache-dir -r ./requirements.txt
COPY ./static /usr/src/app/static/
COPY ./media /usr/src/app/media/
# Copying all the files in our project
COPY . .
