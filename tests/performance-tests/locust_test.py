from locust import HttpUser, task, between
from src.utils.test_images import image_links
import json
import logging


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def testFastApi(self):
        print("img link", image_links[0]["url"])
        image_sample = {
            "img_url":image_links[0]["url"]
        }
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        data = json.dumps(image_sample)
        print(data)
        res = self.client.post("/predict/torch_model/", data=data,
                             headers=headers)
        # response = self.client.get("/")
        # print(response)
        print("res", res)
