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
from PIL import Image

app = Flask(__name__)


@app.route('/segment/<path:base64str>', methods=['POST'])
def segment(base64str):
    if request.method == 'POST':

        output = region_growing.run_region_growing_on_image(base64str)

        return output
    pass


if __name__ == '__main__':
    app.run(debug=True)

# https://jdhao.github.io/2020/04/12/build_webapi_with_flask_s2/
# https://python.plainenglish.io/how-to-send-images-into-flask-api-via-url-7d4be51e8130