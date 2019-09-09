FROM python:3.7-alpine


MAINTAINER Saradhi Nimmagadda

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


CMD python app.py run -h
