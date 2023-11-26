FROM python:3.11-slim
WORKDIR /app

COPY ./run run
COPY ./.env .env
COPY ./requirements.txt requirements.txt
RUN python run --initialization --server

COPY ./src src
CMD python run --production --server