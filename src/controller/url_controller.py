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
        postParser.add_argument('keywords',
           type=int,
           required=True,
           help="This is a required field."
        ) 
        inputData = postParser.parse_args()
        inputData["is_deleted"] = False
 
        if Url.find_url_by_hyperlink(inputData['hyperlink'], inputData['keywords']):
            return {"message": "Posting already found"}, 400

        url = Url(**inputData)
        url.save()

        return {"message": "Posting added successfully."}, 201

    def delete(self):
        postParser = reqparse.RequestParser()
        postParser.add_argument('hyperlink',
           type=str,
           required=True,
           help="This is a required field."
        )
        postParser.add_argument('keywords',
           type=int,
           required=True,
           help="This is a required field."
        )  
        inputData = postParser.parse_args()
         
        url = Url.find_url_by_hyperlink(inputData['hyperlink'], inputData['keywords'])

        url.deleteUrl()
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
	
        return {'urls': list(map(lambda x: x.json(), Url.find_url_by_keywords(inputData['keywords'])))}

