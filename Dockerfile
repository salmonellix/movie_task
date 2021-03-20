# pull official base image
FROM python:3.9-alpine


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