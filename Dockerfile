# pull official base image
FROM python:3.6.4-alpine3.7

RUN apk --update add --no-cache g++ gcc libxslt-dev
RUN pip install --upgrade pip
#RUN pip install lxml
#RUN pip install pandas


# set environment variables
ENV PYTHONUNBUFFERED 1

RUN mkdir /movie_task
WORKDIR /movie_task

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

## copy entrypoint.sh
#COPY ./entrypoint.sh .

# copy project
COPY . .