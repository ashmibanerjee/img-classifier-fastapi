from fastapi.testclient import TestClient
from src.app.app import app
from tests.helpers import *

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World !!!!"}


def test_predict_torch():
    response = predict_test(client, "/predict/torch_model/")
    assert response["status_code"] == 200


def test_predict_tf():
    response = predict_test(client, "/predict/tf/")
    assert response["status_code"] == 200
