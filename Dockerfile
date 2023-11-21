FROM python:3.12-slim
WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./.env .env
COPY ./run run
COPY ./src src
CMD python run --production