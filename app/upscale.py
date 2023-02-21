
import cv2
# from cv2 import dnn_superres
import numpy as np


def upscale(input_path: str, output_path: str, model_path: str = 'EDSR_x2.pb') -> None:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :param model_path: путь к ИИ модели
    :return:
    """

    # scaler = dnn_superres.DnnSuperResImpl_create()
    # scaler.readModel(model_path)
    # scaler.setModel("edsr", 2)

    # Load image as string from file/database
    fd = open(input_path)
    img_str = fd.read()
    fd.close()
    # CV2
    nparr = np.fromstring(img_str, np.uint8)
    img_in = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

    # image = cv2.imread(input_path)
    # result = scaler.upsample(image)
    # cv2.imwrite(output_path, result)
    cv2.imwrite(output_path, img_in)


# def example():
#     upscale('lama_300px.png', 'lama_600px.png')
#
#
# if __name__ == '__main__':
#     example()