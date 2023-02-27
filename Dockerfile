FROM python:3.9

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

COPY ./app /app
WORKDIR /app

# COPY ./app/requirements.txt /app/requirements.txt
# RUN pip3 install --no-cache-dir -r requirements.txt

RUN python -m pip install --upgrade pip
RUN python -m pip install ffmpeg libsm6 libxext6  -y
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT ["/app/run.sh"]

#  ImportError: libGL.so.1: cannot open shared object file: No such file or directory
