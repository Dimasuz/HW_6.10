import time

import requests

print("POST")
response = requests.post(
    "http://127.0.0.1:5000/upscale",
    files={"input_path": open("tests/test.png", "rb")},
)
print(response.status_code)
print(response.text)
task = response.json()
task_id = task["task_id"]
file_id = task["file_in_id"]

task_id = response.json()["task_id"]

print("GET")

status = "PENDING"
while status == "PENDING":
    status = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}").json()["status"]

if status == "SUCCESS":
    img = requests.get(f"http://127.0.0.1:5000/upscale/{file_id}").content
    with open("output.png", "wb") as file:
        file.write(img)
