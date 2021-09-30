# from flask import Flask
# from flask_restful import Api, Resource
import region_growing
# app = Flask(__name__)
# api = Api(app)
#
#
# class Segment(Resource):
#     def get(self, base64):
#         output = region_growing.run_region_growing_on_image(base64)
#         return {"segmented": output}
#
#
# api.add_resource(Segment, "/segment/<string:base64>")
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import request, Flask
from flask_restful import reqparse
import base64

app = Flask(__name__)

base64_string_post_args = reqparse.RequestParser()
base64_string_post_args.add_argument("base64 string", type=str, help="Please input string type")


@app.route('/segment/<path:base64str>', methods=['POST'])
def segment(base64str):
    if request.method == 'POST':
        if isBase64(base64str):
            output = {"segmented Image": region_growing.run_region_growing_on_image(base64str)}
        else:
            output = {"Input Error": "Please Input Base64 String Type"}
        return output
    pass


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
    app.run(debug=True)

# https://jdhao.github.io/2020/04/12/build_webapi_with_flask_s2/
# https://python.plainenglish.io/how-to-send-images-into-flask-api-via-url-7d4be51e8130
