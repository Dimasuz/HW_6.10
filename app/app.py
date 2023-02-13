import datetime
import shutil
import time

from flask import Flask, jsonify, request

from flask.views import MethodView

# from tasks import upscale
from tasks import make_celery




# from errors import ApiError
# from schema import CreateAdv, PatchDelAdv, validate


app = Flask('app')

# celery_app = Celery('tasks', backend='redis://127.0.0.1:6379/2', brocker='redis://127.0.0.1:6379/1')

# @app.errorhandler(ApiError)
# def error_handler(error: ApiError):
#     response = jsonify({"status": "error", "description": error.message})
#     response.status_code = error.status_code
#     return response

# def main():
#     async_result = upscale.delay()
#     print(async_result.task_id)
#     print(async_result.get())

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(flask_app)
# Redis(app)

@celery.task
def upscale(input_path: str, output_path: str):
    with open(input_path, 'a') as f:
        f.write(f'\nstart = {datetime.datetime.now()}\n')
        time.sleep(10)
        f.write(f'finish = {datetime.datetime.now()}\n')
    shutil.copyfile(input_path, output_path)

class PhotoView(MethodView):

    def get(self, photo_id: int):
        print('get')
        return jsonify({'metod': f'get-{photo_id}'})

    def post(self):
        data = request.json
        async_result = upscale.delay(data['input_path'], data['output_path'])
        return jsonify({'async_result.task_id': f'{async_result.task_id}'})


@app.route('/')
@app.route('/index/')
def index():
    return jsonify({'hello': 'Hello, this is my homework Celery!'})


app.add_url_rule('/photo/', view_func=PhotoView.as_view('post_photo'), methods=['POST'])
app.add_url_rule('/photo/<int:photo_id>/', view_func=PhotoView.as_view('get_photo'), methods=['GET'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)