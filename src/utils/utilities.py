from PIL import Image
import os
import requests

current_dir = os.getcwd()
os.chdir(current_dir + "/../")


def dir_check(dir_location):
    isExist = os.path.exists(dir_location)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(dir_location)
        print("The new directory is created!")
    else:
        print("directory already exists!")


def load_image(img_url):
    try:
        img = Image.open(requests.get(img_url, stream=True).raw)
        return img
    except Exception as e:
        print(e)
        print("image could not be opened")
