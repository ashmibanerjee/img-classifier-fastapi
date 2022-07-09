from src.utils.test_images import image_links
import json
from src.schemas.image_schema import Img


def predict_test(client, api_url):
    sample = Img(img_url=image_links[0]["url"])
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    res = client.post(api_url,
                      data=json.dumps(sample.dict()),
                      headers=headers)

    return res.json()
