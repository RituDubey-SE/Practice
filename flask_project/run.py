from flask import Flask
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class SimpleFlask(Resource):

    def get(self):
        return"simple get method"
    def post(self):
        return "simple post method"

api.add_resource(SimpleFlask, '/firstpage')

if __name__ == "__main__":
    app.run(debug=True)