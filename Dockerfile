FROM python:3.9-alpine

WORKDIR app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./app/requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app /app

ENTRYPOINT ["/app/run.sh"]

