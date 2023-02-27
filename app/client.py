import time

import requests

print("POST")
response = requests.post(
    "http://127.0.0.1:5000/upscale",
    files={"input_path": open("lama_300px.png", "rb")},
)

print(response.status_code)
print(response.json())

task_id = response.json()["task_id"]

print("GET")
response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")

print(response.status_code)
print(response.json())

while "PENDING" in response.text:
    time.sleep(5)
    response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
    print(response.status_code)
    print(response.json())
