import base64

import requests

BASE = "http://127.0.0.1:5000/"


def img2string(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        image_string = encoded_string.decode('utf-8')
        response = requests.post(BASE + "segment/" + image_string)
        print(response.json())



response = requests.post(BASE + "segment/sds")
print(response.json())

for i in range(1, 10):
    img2string("testing_images/mdb00" + str(i) + ".pgm")
