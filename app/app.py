import os
import datetime
import time

from flask_pymongo import PyMongo
from celery.result import AsyncResult
from flask import Flask, jsonify, request

from flask.views import MethodView
from celery import Celery
from werkzeug.utils import secure_filename
# import config
from upscale import upscale

app = Flask('app')

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/1'
app.config['UPLOAD_FOLDER'] = 'files'
app.config['MONGO_DSN'] = 'mongodb://app:123@localhost:27017/files?authSource=admin'

celery_app = Celery(app.name, backend= app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])

celery_app.conf.update(app.config)

mongo = PyMongo(app, uri=app.config['MONGO_DSN'])

class ContextTask(celery_app.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery_app.Task = ContextTask


@celery_app.task
def upscale_app(input_path: str, output_path: str, mongo):
    upscale(input_path, output_path, mongo)
#     with open(input_path, 'a') as f:
#         f.write(f'\nstart = {datetime.datetime.now()}\n')
#         time.sleep(2)
#         f.write(f'finish = {datetime.datetime.now()}\n')
#         # path_file = str(mongo.save_file(f"{nanoid.generate()}{output_path}", f))
#         # print(f'{path_file=}')
#     shutil.copyfile(input_path, output_path)

# # @app.errorhandler(ApiError)
# # def error_handler(error: ApiError):
# #     response = jsonify({"status": "error", "description": error.message})
# #     response.status_code = error.status_code
# #     return response
#
#
class PhotoView(MethodView):

    def get(self, task_id: str):
        task = AsyncResult(task_id, app=celery_app)
        if task.status == ' SUCCESS':
            return jsonify({"status": task.status, "result": task.result})
        return jsonify({"status": task.status})

    def post(self):
        output_path = 'output_path'

        # input_path = secure_filename(file_in.filename)
        # # print(filename_in)
        if 'input_path' in request.files:
            file_in = request.files.get('input_path')
            file_in_name = f"{datetime.datetime.now()}-{file_in.filename}"
            input_path = str(mongo.save_file(file_in_name, file_in))

        # input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename_in)
        # print(f'{input_path=}')
        # file_in.save(input_path)
        print(f'{input_path=}')
        print(f'{output_path=}')
        print(f'{file_in_name=}')

        file_inn = mongo.send_file(file_in_name)
        with open(file_inn, 'a') as f:
            f.write(f'\nstart = {datetime.datetime.now()}\n')
            time.sleep(2)
            f.write(f'finish = {datetime.datetime.now()}\n')
        # shutil.copyfile(input_path, output_path)
        file_out_name = f"{datetime.datetime.now()}-{output_path}"
        file_out = str(mongo.save_file(file_out_name, file_inn))

        # async_result = upscale_app.delay(input_path, output_path)
        # async_result = upscale_app(input_path, output_path, mongo)
        # print(f'{async_result.task_id=}')
        # return jsonify({'task_id': async_result.task_id})
        return jsonify({'status': 'OK', 'file_out': file_out})


# @app.route("/processed/<path: file>")
# def get_photo(file):
#     # безопасно соединяем базовый каталог и имя файла
#     safe_path = safe_join(app.config["CSV_FOLDER"], filename)
#     try:
#         return send_file(safe_path, as_attachment=True)
#     except FileNotFoundError:
#         abort(404)

#
@app.route('/')
@app.route('/index/')
def index():
    return jsonify({'hello': 'Hello, this is my homework Celery!'})


app.add_url_rule('/upscale', view_func=PhotoView.as_view('post_photo'), methods=['POST'])
app.add_url_rule('/tasks/<task_id>', view_func=PhotoView.as_view('get_photo'), methods=['GET'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
