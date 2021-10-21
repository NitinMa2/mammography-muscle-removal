import base64
import requests
import json

BASE = "http://127.0.0.1:5000/segment"


def img2string(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        image_string = encoded_string.decode('utf-8')
        payload = json.dumps({
            "base64Image": image_string
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", BASE, headers=headers, data=payload)
        return response.json()


if __name__ == "__main__":
    print("---Testing valid parameters---")
    for i in range(1, 10):
        output_base64 = img2string("testing_images/mdb00" + str(i) + ".pgm")
        print(output_base64)
    print("\n---Testing Invalid parameters")
    invalid_args = ["notvalidbase64", "965945", "/+=2", ""]
    for i in invalid_args:
        payload = json.dumps({
            "base64Image": i
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", BASE, headers=headers, data=payload)
        print(response.json())
    print("\n---Testing Invalid api method")
    payload = json.dumps({
        "base64Image": "anystring"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", BASE, headers=headers, data=payload)
    print(response.json())
    print("\n---Testing Invalid api endpoint")
    response = requests.post(BASE + "/ok")
    print(response.json())