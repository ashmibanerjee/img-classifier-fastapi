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


def tf_predict(img_original):
    img = img_original
    img = img.resize(IMAGE_SHAPE)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    img = np.array(img) / 255
    model = load_model()
    result = model.predict(img[np.newaxis, ...])
    predicted_class = tf.math.argmax(result[0], axis=-1)
    labels_path = tf.keras.utils.get_file('ImageNetLabels.txt',
                                          'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    imagenet_labels = np.array(open(labels_path).read().splitlines())
    predicted_class_name = imagenet_labels[predicted_class]
