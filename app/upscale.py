import datetime
import shutil
import time


def upscale(input_path: str, output_path: str, mongo):
    file_in = mongo.send_file(input_path)
    with open(file_in, 'a') as f:
        f.write(f'\nstart = {datetime.datetime.now()}\n')
        time.sleep(2)
        f.write(f'finish = {datetime.datetime.now()}\n')
    # shutil.copyfile(input_path, output_path)
    file_out = str(mongo.save_file(f"{datetime.datetime.now()}-{output_path}", file_in))
# import cv2
# from cv2 import dnn_superres


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


# def example():
#     upscale('lama_300px.png', 'lama_600px.png')
#
#
# if __name__ == '__main__':
#     example()