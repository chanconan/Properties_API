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

    def post(self):
        # Get properties or options from post data. Can be used for handling sort options with price, num of bedrooms
        # and newest is by default.
        request_data = request.get_json()
        if request_data['ascending'].lower() == "false":
            ascending = False
        else:
            ascending = True
        
        if request_data['sortBy'] == "price":
            allProperties = data.sort_values(by=["PRICE"], ascending=ascending)
        elif request_data['sortBy'] == "bedrooms":
            allProperties = data.sort_values(by["BEDS"], ascending=ascending)
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
