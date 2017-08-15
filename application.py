from flask import Flask
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


class Hello_World(Resource):
    def get(self):
        return "hello world"


class Food(Resource):
    def get(self, value):
        return "you input: {}".format(value)

api.add_resource(Hello_World, '/')
api.add_resource(Food, '/food/<value>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
