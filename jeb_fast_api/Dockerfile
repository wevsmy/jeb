#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8

COPY . /app

RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /app/requirements.txt --no-cache-dir

WORKDIR /app

ENV PYTHONPATH=/app

VOLUME ["/app/logs"]

EXPOSE 80
