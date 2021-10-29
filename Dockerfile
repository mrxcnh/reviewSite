FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
RUN ls -la