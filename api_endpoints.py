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
        all_properties = data.sort_values(by=["DAYS ON MARKET"], ascending=True)
        all_properties = all_properties.to_json(orient="index")
        return all_properties, 200

    def post(self):
        # Get properties or options from post data. Can be used for handling sort options with price, num of bedrooms
        # and newest is by default. Also checks if sort is in descending or ascending

        request_data = request.get_json()
        if request_data['ascending'].lower() == "false":
            ascending = False
        else:
            ascending = True

        if request_data['sortBy'] == "price":
            all_properties = data.sort_values(by=["PRICE"], ascending=ascending)
        elif request_data['sortBy'] == "bedrooms":
            all_properties = data.sort_values(by["BEDS"], ascending=ascending)
        all_properties = all_properties.to_json(orient="index")

        return all_properties, 200

class PropertyById(Resource):
    def get(self, id):
        single_property = data.to_dict(orient="index")[id]
        return single_property, 200

class PropertyVotes(Resource):
    def post(self, id):
        vote_method = request.get_json()["vote"].lower()
        single_property = data.to_dict(orient="index")[id]
        if vote_method == "upvote":
            single_property['UPVOTE'] = single_property['UPVOTE'] + 1
        elif vote_method == "downvote":
            single_property['DOWNVOTE'] = single_property['DOWNVOTE'] + 1
        return 200

api.add_resource(Properties, '/properties')
api.add_resource(PropertyById, '/properties/<int:id>')
api.add_resource(PropertyVotes, '/properties/vote/<int:id>')

if __name__ == '__main__':
    app.run()  # run our Flask app
