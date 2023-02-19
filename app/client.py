import requests
import time


print('POST')
response = requests.post('http://127.0.0.1:5000/upscale',
                        files={"input_path": open("start.txt", "rb")},
                        )

print(response.status_code)
# print(response.json())
# print(response.text)

# task_id = response.json()['task_id']
# print(task_id)
#
#
# print('GET')
# response = requests.get(f'http://127.0.0.1:5000/tasks/{task_id}')
#
# print(response.status_code)
# print(response.text)
#
# time.sleep(3)
#
# response = requests.get(f'http://127.0.0.1:5000/tasks/{task_id}')
#
# print(response.status_code)
# print(response.text)
#
