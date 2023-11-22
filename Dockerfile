FROM python:3.12-slim
WORKDIR /app

COPY ./run run
COPY ./requirements.txt requirements.txt
RUN python run --initialization --server

COPY ./.env .env
COPY ./src src
CMD python run --production --server