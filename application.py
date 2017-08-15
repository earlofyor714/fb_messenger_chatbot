from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import requests

import os
import sys
import json

app = Flask(__name__)
api = Api(app)


class Hello_World(Resource):
    def get(self):
        if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
            if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
                log("token mismatch")
                return "Verification token mismatch", 403
            log("hub challenge: {}".format(request.args["hub.challenge"]))
            return request.args["hub.challenge"], 200
        return "hello world", 200


class Food(Resource):
    def get(self, value):
        return "you input: {}".format(value)


def log(message):
    print(str(message))
    sys.stdout.flush()

api.add_resource(Hello_World, '/')
api.add_resource(Food, '/food/<value>')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=True)
