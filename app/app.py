from bson.objectid import ObjectId
from cachetools import cached
from celery.result import AsyncResult
from config import (CELERY_BROKER_URL, CELERY_RESULT_BACKEND,
                    MAX_CONTENT_LENGTH, MONGO_DSN)
from flask import Flask, jsonify, request, send_file
from flask.views import MethodView
from flask_pymongo import PyMongo
from gridfs import GridFS
from nanoid import generate
from tasks import celery_app, upscale_app
from werkzeug.utils import secure_filename

app = Flask("app")

app.config["CELERY_BROKER_URL"] = CELERY_BROKER_URL
app.config["CELERY_RESULT_BACKEND"] = CELERY_RESULT_BACKEND
app.config["MONGO_DSN"] = MONGO_DSN
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

celery_app.conf.update(app.config)

mongo = PyMongo(app, uri=app.config["MONGO_DSN"])


@cached({})
def get_fs():
    return GridFS(mongo.db)


ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


def file_save(file_name: str, file) -> str:
    """save file in mongo"""
    return str(mongo.save_file(file_name, file))


def file_read(file_id: str):
    """get file from mongo"""
    files = get_fs()
    file = files.get(ObjectId(file_id))
    return file.name, file


class PhotoView(MethodView):
    def get(self, file_id: str):
        filename, file = file_read(file_id)
        return send_file(file, as_attachment=False, download_name=filename)

    def post(self):
        if "input_path" in request.files:
            file = request.files.get("input_path")
            file_name = secure_filename(file.filename)
            if not allowed_file(file_name):
                return jsonify({"status": "404 - wrong type of the file"})
            file_in_name = f"{generate(size=5)}_{file_name}"
            file_in_id = file_save(file_in_name, file)
        else:
            return jsonify({"status": "404 - file not found"})

        async_result = upscale_app.delay(file_in_id)
        return jsonify({"task_id": async_result.task_id})


#
@app.route("/")
@app.route("/index/")
def index():
    return jsonify({"hello": "Hello, this is my homework Celery!"})


@app.route("/tasks/<string:task_id>")
def get_task(task_id: str):
    task = AsyncResult(task_id, app=celery_app)
    if task.status == "SUCCESS":
        return jsonify({"status": task.status, "file_id": task.result})
    return jsonify({"status": task.status})


photo_view = PhotoView.as_view("photo_view")
app.add_url_rule("/upscale", view_func=photo_view, methods=["POST"])
app.add_url_rule("/upscale/<string:file_id>", view_func=photo_view, methods=["GET"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
