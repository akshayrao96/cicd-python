FROM python:3.12-slim
RUN apt update
RUN apt-get install -y git
RUN pip install poetry
WORKDIR /app