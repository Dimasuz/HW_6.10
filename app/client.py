import time

import requests

print("POST")
response = requests.post(
    "http://127.0.0.1:5000/upscale",
    files={"input_path": open("test.png", "rb")},
)

print(response.status_code)
print(response.json())

task_id = response.json()["task_id"]

print("GET")

status = "PENDING"

while status == "PENDING":
    time.sleep(5)
    response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
    status = response.json()["status"]
    print(response.status_code)
    print(response.json())
