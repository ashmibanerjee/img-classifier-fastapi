from locust import HttpUser, task, between
from src.utils.test_images import image_links
import json
from src.schemas.image_schema import Img


class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    def predict(self, url):
        sample = Img(img_url=image_links[0]["url"])
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        res = self.client.post(url,
                               data=json.dumps(sample.dict()),
                               headers=headers)

        return res.json()

    @task(1)
    def test_fastapi(self):
        response = self.client.get("/")
        print(response.json())

    @task(2)
    def test_torch_predict(self):
        res = self.predict("/predict/torch_model/")
        print("res", res)

    @task(3)
    def test_tf_predict(self):
        res = self.predict("/predict/tf/")
        print("res", res)


