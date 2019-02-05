FROM python:3.7.2-stretch

ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
