import io

import pymongo
from bson.objectid import ObjectId
from cachetools import cached
from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND, MONGO_DSN
from gridfs import GridFS
from upscale import upscale

celery_app = Celery(
    "app",
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
)


@cached({})
def get_fs():
    mongo = pymongo.MongoClient(MONGO_DSN)
    return GridFS(mongo["files"])


def file_save(file_name: str, file) -> str:
    """save file in mongo"""
    files = get_fs()
    file = files.put(file, filename=file_name)
    return str(file)


def file_read(file_id: str):
    """get file from mongo"""
    files = get_fs()
    file = files.get(ObjectId(file_id))
    return file.name, file


@celery_app.task
def upscale_app(file_in_id):
    file_in_name, file_in = file_read(file_in_id)
    file_in = file_in.read()
    file_out_name = f"image_out-{file_in_name}"
    file_out = upscale(file_in)
    file_out = io.BytesIO(file_out)
    file_out_id = file_save(file_out_name, file_out.getvalue())
    return file_out_id

# celery -A tasks.celery_app worker -l info -P gevent