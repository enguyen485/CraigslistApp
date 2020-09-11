from flask_restful import Resource, reqparse
from models.url import Url	
import datetime
class Urls(Resource):


    def post(self):
        postParser = reqparse.RequestParser()
        postParser.add_argument('hyperlink',
           type=str,
           required=True,
           help="This is a required field."
        )
        postParser.add_argument('craigslist_id',
           type=int,
           required=True,
           help="This is a required field."
        )   
        postParser.add_argument('keywords',
           type=int,
           required=True,
           help="This is a required field."
        )  
        postParser.add_argument('date',
           type=str,
           required=True,
           help="This is a required field."
        )  
        inputData = postParser.parse_args()
 
        if Url.find_url_by_id(inputData['craigslist_id'], inputData['keywords']):
            return {"message": "Posting already found"}, 400

        url = Url(**inputData)
        url.save()

        return {"message": "Posting added successfully."}, 201

    def get(self):
        getParser = reqparse.RequestParser()
        getParser.add_argument('keywords',
           type=int,
           required=True,
           help="This is a required field."
        )
        inputData = getParser.parse_args()
	
        return {'Urls': list(map(lambda x: x.json(), Url.find_url_by_keywords(inputData['keywords'])))}

