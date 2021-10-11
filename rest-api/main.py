import region_growing
from flask import request, Flask
from flask_restful import reqparse
import base64
from flask import abort, jsonify

'''
Pectoral Muscle Segmentation API
Valid Methods = POST
Valid Endpoint = Segment
http://127.0.0.1:5000/segment/{base64_string}
This Post Method with segment endpoint takes in a base64 encoded image in string format 
and gives a json response with the segmented image in base64 encoded string.
A valid API call example will look like
http://127.0.0.1:5000/segment/{base64_string}
with response
{"segmentedImage" : "base_64_image_string"}
'''
app = Flask(__name__)

base64_string_post_args = reqparse.RequestParser()
base64_string_post_args.add_argument("base64 string", type=str, help="Please input string type")


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(500)
def internal_server_error(e):
    return {"Internal Server Error": "Please check your url or parameters"}


@app.errorhandler(405)
def method_not_allowed(e):
    return {"Method not Allowed Error": "This method is not supported by the API"}


@app.route('/segment', methods=['POST'])
def segment():
    base64str = request.get_json()["base64Image"]

    if base64str is None:
        abort(404, description="Resource not found")
        return jsonify(base64str)

    if request.method == 'POST':
        if isBase64(base64str):
            output = {"segmentedImage": region_growing.run_region_growing_on_image(base64str)}
        else:
            output = {"Input Error": "Please Input Base64 String Type"}
        return output
    if request.method != 'POST':
        output = {"Method not Allowed Error": "This method is not supported by the API"}
        return output
    output = {"Internal Server Error": "Please Check your input parameters"}

    return output


def isBase64(sb):
    try:
        if isinstance(sb, str):
            # If there's any unicode here, an exception will be thrown and the function will return false
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False


if __name__ == '__main__':
    app.run(debug=False)