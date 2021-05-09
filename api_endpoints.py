from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)

class Properties(Resource):
    def get(self):
        data = pd.read_csv('properties.csv')
        data = data.to_json(orient="index")
        return data, 200

api.add_resource(Properties, '/properties')
if __name__ == '__main__':
    app.run()  # run our Flask app
