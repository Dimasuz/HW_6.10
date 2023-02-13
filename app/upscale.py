from celery import Celery

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery





# import datetime
# import shutil
# import time

import cv2
from cv2 import dnn_superres



# def upscale(input_path: str, output_path: str, model_path: str = 'EDSR_x2.pb') -> None:
#     """
#     :param input_path: путь к изображению для апскейла
#     :param output_path:  путь к выходному файлу
#     :param model_path: путь к ИИ модели
#     :return:
#     """
#
#     scaler = dnn_superres.DnnSuperResImpl_create()
#     scaler.readModel(model_path)
#     scaler.setModel("edsr", 2)
#     image = cv2.imread(input_path)
#     result = scaler.upsample(image)
#     cv2.imwrite(output_path, result)
#

# def upscale(input_path: str, output_path: str) -> None:
#     with open(input_path, 'a') as f:
#         f.write(f'\nstart = {datetime.datetime.now()}\n')
#         time.sleep(1)
#         f.write(f'finish = {datetime.datetime.now()}\n')
#     shutil.copyfile(input_path, output_path)


# def example(input_path: str, output_path: str):
#     start = datetime.datetime.now()
#     print(f'{start=}')
#     # upscale('lama_300px.png', 'lama_600px.png')
#     upscale(input_path, output_path)
#     print(f'всего = {datetime.datetime.now() - start}')


