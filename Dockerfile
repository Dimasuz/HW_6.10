FROM python:3.9

COPY ./app /app
WORKDIR /app

RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/

RUN python -m pip install --upgrade pip

RUN python -m pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT bash run.sh
