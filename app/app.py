from flask import Flask, jsonify, request

from flask.views import MethodView

from tasks import upscale
# from tasks import make_celery




app = Flask('app')


# @app.errorhandler(ApiError)
# def error_handler(error: ApiError):
#     response = jsonify({"status": "error", "description": error.message})
#     response.status_code = error.status_code
#     return response


class PhotoView(MethodView):

    def get(self, photo_id: int):
        print('get')
        return jsonify({'metod': f'get-{photo_id}'})

    def post(self):
        data = request.json
        print(data)
        # async_result = upscale.delay(data['input_path'], data['output_path'])
        # return jsonify({'async_result.task_id': f'{async_result.task_id}'})
        result = upscale(data['input_path'], data['output_path'])

        return jsonify(status='OK')


@app.route('/')
@app.route('/index/')
def index():
    return jsonify({'hello': 'Hello, this is my homework Celery!'})


app.add_url_rule('/photo/', view_func=PhotoView.as_view('post_photo'), methods=['POST'])
app.add_url_rule('/photo/<int:photo_id>/', view_func=PhotoView.as_view('get_photo'), methods=['GET'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)