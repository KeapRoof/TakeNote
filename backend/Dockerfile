FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install aiomysql
RUN pip install cryptography



COPY . /app
