from flask import Flask, request
from src.pred.image_classifier import *

app = Flask(__name__)


@app.route('/')
def read_main():
    return {"msg": "Hello World !!!!"}


@app.route("/predict/", methods=["POST"])
def predict_api(img_url: str):
    if request.method == "POST":
        prediction = torch_run_classifier(img_url)
        if not prediction:
            return {
                "status_code": 404,
                "detail": "Image could not be downloaded"
            }

        return {"predicted_label": prediction[0],
                "probability": prediction[1]}


if __name__ == '__main__':
    app.run(debug=True)
