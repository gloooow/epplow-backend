FROM python:3.11-bullseye

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

