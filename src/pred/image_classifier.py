from PIL import Image
import requests
import torch
from torchvision import models
from torchvision import transforms
import os

current_dir = os.getcwd()
os.chdir(current_dir + "/../")
IMG_SAVE_LOCATION = os.getcwd() + "/resources/"


def run_classifier(image):
    img = load_image(image)  # loading image
    if img is None:
        return None
    input_batch = preprocess(img)  # preprocessing image
    top_labels = predict(input_batch, model=None)  # prediction
    return top_labels[0]


def dir_check(dir_location=IMG_SAVE_LOCATION):
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


def preprocess(img):
    try:
        transform = transforms.Compose([  # [1]
            transforms.Resize(256),  # [2]
            transforms.CenterCrop(224),  # [3]
            transforms.ToTensor(),  # [4]
            transforms.Normalize(  # [5]
                mean=[0.485, 0.456, 0.406],  # [6]
                std=[0.229, 0.224, 0.225]  # [7]
            )])
        input_tensor = transform(img)
        input_batch = torch.unsqueeze(input_tensor, 0)
        return input_batch
    except Exception as e:
        print(e)


model = None


def get_model():
    global model
    if model is None:
        model = models.alexnet(pretrained=True)
    return model


def get_labels():
    if not os.path.exists(IMG_SAVE_LOCATION + 'imagenet_classes.txt'):
        dir_check(IMG_SAVE_LOCATION)
        print("downloading imgnet classes in: ", IMG_SAVE_LOCATION)
        url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
        r = requests.get(url, allow_redirects=True)
        open(IMG_SAVE_LOCATION + 'imagenet_classes.txt', 'wb').write(r.content)

    with open(IMG_SAVE_LOCATION + 'imagenet_classes.txt') as f:
        labels = [line.strip() for line in f.readlines()]
    return labels


def predict(input_batch, model=None):
    if model is None:
        model = get_model()
    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    model.eval()
    with torch.no_grad():
        output = model(input_batch)
    # Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
    # print(output[0])

    labels = get_labels()
    _, index = torch.max(output, 1)

    percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100

    # print(labels[index[0]], percentage[index[0]].item())

    _, indices = torch.sort(output, descending=True)
    return [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]
