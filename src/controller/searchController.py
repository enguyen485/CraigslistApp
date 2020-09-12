from flask_restful import Resource, reqparse
from models.searches import Search	
import datetime
class Searches(Resource):



    def post(self):
        postParser = reqparse.RequestParser()
        postParser.add_argument('keywords',
            type=str,
            required=True,
            help="This is a required field."
        )
        postParser.add_argument('min_price',
            type=int,
            required=True,
            help="This is a required field."
        )
        postParser.add_argument('max_price',
            type=int,
            required=True,
            help="This is a required field."
        ) 
        inputData = postParser.parse_args()

        if Search.find_searches_by_keywords(inputData['keywords']):
            return {"message": "Search already exists"}, 400

        search = Search(**inputData)
        search.save()

        return {"message": "Search added successfully."}, 201

    def get(self):
	
        return {"searches": list(map(lambda x: x.json(), Search.find_all_searches()))}

