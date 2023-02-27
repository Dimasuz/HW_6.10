
import pytest
import time
import requests

def test_():

    """POST"""
    response = requests.post(
        "http://127.0.0.1:5000/upscale",
        files={"input_path": open("lama_300px.png", "rb")},
    )
    assert response.status_code == 200

    """GET TASK"""
    task_id = response.json()["task_id"]
    response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
    assert response.json()["status"] == "PENDING"
    k = 0
    while k < 20:
        k += 1
        time.sleep(10)
        response = requests.get(f"http://127.0.0.1:5000/tasks/{task_id}")
        if "SUCCESS" in response.json()["status"]:
            k = 20
    assert response.json()["status"] == "SUCCESS"

    """GET FILE"""
    if response.json()["status"] == "SUCCESS":
        file_id = response.json()["file_id"]
        resp = requests.get(f"http://127.0.0.1:5000/upscale/{file_id}")
    assert resp.status_code == 200


