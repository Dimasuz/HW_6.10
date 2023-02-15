import datetime
import shutil
import time

# # import cv2
# # from cv2 import dnn_superres

import celery

celery_app = celery.Celery('tasks', backend='redis://127.0.0.1:6379/2', brocker='redis://127.0.0.1:6379/1')

# @app.tasks
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


def upscale(input_path: str, output_path: str):
    with open(input_path, 'a') as f:
        f.write(f'\nstart = {datetime.datetime.now()}\n')
        time.sleep(2)
        f.write(f'finish = {datetime.datetime.now()}\n')
    shutil.copyfile(input_path, output_path)
