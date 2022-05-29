from fastapi import FastAPI, HTTPException
from src.pred.image_classifier import *

app = FastAPI(title="Image Classifier API")


@app.get("/")
async def read_main():
    return {"msg": "Hello World !!!!"}


@app.post("/predict/torch_model/", status_code=200)
async def predict_torch(img_url: str):
    prediction = torch_run_classifier(img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return {"predicted_label": prediction[0],
            "probability": prediction[1]}


@app.post("/predict/tf/", status_code=200)
async def predict_tf(img_url: str):
    prediction = tf_run_classifier(img_url)
    if not prediction:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail="Image could not be downloaded"

        )

    return prediction
