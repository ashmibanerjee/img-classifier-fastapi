from src.utils.utilities import *
import os
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

SAVE_LOCATION = os.getcwd() + "/resources/"
IMAGE_SHAPE = (224, 224)


def load_model():
    mobilenet_v2 = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
    classifier_model = mobilenet_v2

    classifier = tf.keras.Sequential([
        hub.KerasLayer(classifier_model, input_shape=IMAGE_SHAPE + (3,))
    ])
    return classifier


def preprocess_img(img):
    img = img.resize(IMAGE_SHAPE)
    img = np.array(img) / 255
    return img


def load_labels():
    labels_path = tf.keras.utils.get_file('ImageNetLabels.txt',
                                          'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    imagenet_labels = np.array(open(labels_path).read().splitlines())
    return imagenet_labels


def tf_predict(img_original):

    img = preprocess_img(img_original)

    model = load_model()
    result = model.predict(img[np.newaxis, ...])
    predicted_class = tf.math.argmax(result[0], axis=-1)
    scores = tf.nn.softmax(result[0])
    probability = np.max(scores)

    imagenet_labels = load_labels()
    predicted_class_name = imagenet_labels[predicted_class]

    return {"predicted_label": predicted_class_name,
            "probability": probability.item()}
