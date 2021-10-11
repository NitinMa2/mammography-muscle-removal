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
    return jsonify(message="Internal Server Error"), 500


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(message="Method Not Allowed"), 405


def create_error_message(message, status_code=400):
    return {
        "error": {
            "status": status_code,
            "message": message
        }
    }


@app.route('/segment', methods=['POST'])
def segment():
    response = None
    status_code = None

    if request.get_json():
        if 'base64Image' in request.get_json():
            base64str = request.get_json()["base64Image"]
        else:
            base64str = None
            response = create_error_message("Please ensure your request body includes the base64Image attribute")
    else:
        base64str = None
        response = create_error_message("Please ensure your request body includes a JSON object")

    if base64str is None:
        status_code = 400
        if response is None:
            abort(500)  # Internal Server Error
    else:
        if request.method == 'POST':
            if is_base64(base64str):
                status_code = 200
                response = {"segmentedImage": region_growing.run_region_growing_on_image(base64str)}
            else:
                status_code = 400
                response = create_error_message("Please ensure your request includes a valid base64 string")
        else:
            status_code = 405
            response = create_error_message("The URL does not support the " + request.method + " method", status_code)

    if status_code is None or response is None:
        abort(500)  # Internal Server Error

    return response, status_code


def is_base64(sb):
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
    app.run(debug=True)