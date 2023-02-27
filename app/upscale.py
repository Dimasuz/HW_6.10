import cv2
import numpy as np
from cachetools import cached
from cv2 import dnn_superres


@cached({})
def get_model(model_path):
    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    return scaler


def upscale(file_in, model_path: str = "EDSR_x2.pb"):
    """
    :param file_in: принимаемый файл-объект для обработки
    :param file_out:  возвращаемый файл-объект после обработки
    :param model_path: путь к ИИ модели
    :return:
    """

    scaler = get_model(model_path)

    # декодирование входящего изображения
    nparr = np.fromstring(file_in, np.uint8)
    image_in = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    result = scaler.upsample(image_in)

    # кодирование исходящего изображения
    res, file_out = cv2.imencode(".png", result)

    return file_out
