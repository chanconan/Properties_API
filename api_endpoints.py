from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import pandas as pd
import json

app = Flask(__name__)
api = Api(app)
data = pd.read_csv('properties.csv')
data['UPVOTE'] = 0
data['DOWNVOTE'] = 0
data['NET VOTES'] = data['UPVOTE'] - data['DOWNVOTE']
data['TOTAL VOTES'] = data['UPVOTE'] + data['DOWNVOTE']

# Since the code is not saved in an actual Database, the changes made to the properties are reset
# whenever the Flask server is redeployed.
class Properties(Resource):
    # Filtered out all data into a smaller dataframe, listing most of the essentials a user want to look at
    properties_data = data[['PROPERTY TYPE', 'ADDRESS','PRICE', 'BEDS', 'BATHS', 'STATUS', 'UPVOTE', 'DOWNVOTE', 'NET VOTES', 'TOTAL VOTES', 'DAYS ON MARKET']]
    
    # By default, sort properties by newest
    def get(self):
        all_properties = self.properties_data.sort_values(by=["DAYS ON MARKET"], ascending=True)
        all_properties = all_properties.to_dict(orient="index")
        return all_properties, 200

    def post(self):
        # Get properties or options from post data. Can be used for handling sort options with price, num of bedrooms
        # and newest is by default. Also checks if sort is in descending or ascending

        request_data = request.get_json()
        sort = request_data['sortBy'].lower()
        if request_data['ascending'].lower() == "false":
            ascending = False
        else:
            ascending = True

        if sort == "price":
            all_properties = self.properties_data.sort_values(by=["PRICE"], ascending=ascending)
        elif sort == "bedrooms":
            all_properties = selfproperties_data.sort_values(by=["BEDS"], ascending=ascending)
        elif sort == "net":
            all_properties = self.properties_data.sort_values(by=["NET VOTES", "DAYS ON MARKET"], ascending=(ascending, True))
        elif sort == "total":
            all_properties = self.properties_data.sort_values(by=["TOTAL VOTES", "DAYS ON MARKET"], ascending=(ascending, True))
        all_properties = all_properties.to_dict(orient="index")

        return all_properties, 200

class PropertyById(Resource):
    def get(self, id):
        print(data.loc[id]['UPVOTE'])
        single_property = data.to_dict(orient="index")[id]
        return single_property, 200

class PropertyVotes(Resource):
    def post(self, id):
        vote_method = request.get_json()["vote"].lower()
        if vote_method == "upvote":
            data.at[id, 'UPVOTE'] = data.at[id, 'UPVOTE'] + 1
        elif vote_method == "downvote":
            data.at[id, 'DOWNVOTE'] = data.at[id, 'DOWNVOTE'] + 1
        data.at[id, 'NET VOTES'] = data.at[id, 'UPVOTE'] - data.at[id, 'DOWNVOTE']
        data.at[id, 'TOTAL VOTES'] = data.at[id, 'UPVOTE'] + data.at[id, 'DOWNVOTE']
        return 200

api.add_resource(Properties, '/properties')
api.add_resource(PropertyById, '/properties/<int:id>')
api.add_resource(PropertyVotes, '/properties/vote/<int:id>')

if __name__ == '__main__':
    app.run()  # run our Flask app
