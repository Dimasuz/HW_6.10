import time

import pytest
from bson.objectid import ObjectId

from app import app, get_fs


@pytest.fixture()
def get_app():
    # app = app()
    app.config.update(
        {
            "TESTING": True,
        }
    )
    yield app


@pytest.fixture()
def client(get_app):
    return app.test_client()


def test_(client):
    """POST"""
    response = client.post(
        "http://127.0.0.1:5000/upscale",
        data={"input_path": open("tests/test.png", "rb")},
    )
    assert response.status_code == 200
    assert response.json["task_id"]

    """GET TASK"""
    task_id = response.json["task_id"]
    file_in_id = response.json["file_in_id"]
    response = client.get(f"http://127.0.0.1:5000/tasks/{task_id}")
    assert response.json["status"] in ["PENDING", "SUCCESS"]
    k = 0
    while k < 20:
        k += 1
        time.sleep(10)
        response = client.get(f"http://127.0.0.1:5000/tasks/{task_id}")
        if "SUCCESS" in response.json["status"]:
            k = 20
        else:
            response = client.get(f"http://127.0.0.1:5000/tasks/{task_id}")
    assert response.json["status"] == "SUCCESS"
    assert response.json["file_id"]

    """GET FILE"""
    file_id = response.json["file_id"]
    response = client.get(f"http://127.0.0.1:5000/upscale/{file_id}")
    files = get_fs()
    files.delete(ObjectId(file_in_id))
    files.delete(ObjectId(file_id))
    assert response.status_code == 200
    assert response.data
