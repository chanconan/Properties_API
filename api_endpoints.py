from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)
data = pd.read_csv('properties.csv')
data['UPVOTE'] = 0
data['DOWNVOTE'] = 0

class Properties(Resource):
    def get(self):
        allProperties = data.sort_values(by=["DAYS ON MARKET"], ascending=True)
        allProperties = allProperties.to_json(orient="index")
        return allProperties, 200

class PropertyById(Resource):
    def get(self, id):
        singleProperty = data.to_dict()
        prop = {}
        for field in singleProperty:
            prop[field] = singleProperty[field][id]
        return {id:prop}, 200

api.add_resource(Properties, '/properties')
api.add_resource(PropertyById, '/properties/<int:id>')

if __name__ == '__main__':
    app.run()  # run our Flask app
