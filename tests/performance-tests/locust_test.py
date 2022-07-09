from locust import HttpUser, task, between
from tests.helpers import *


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_fastapi(self):
        response = self.client.get("/")
        print(response.json())

    @task(2)
    def test_torch_predict(self):
        res = predict_test(self.client, "/predict/torch_model/")
        print("res", res)

    @task(3)
    def test_tf_predict(self):
        res = predict_test(self.client, "/predict/tf/")
        print("res", res)
