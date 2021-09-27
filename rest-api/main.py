from flask import Flask
from flask_restful import Api, Resource
import region_growing
app = Flask(__name__)
api = Api(app)


class Segment(Resource):
    def get(self, base64):
        output = region_growing.run_region_growing_on_image(base64)
        return {"segmented": output}


api.add_resource(Segment, "/segment/<string:base64>")
if __name__ == "__main__":
    app.run(debug=True)
