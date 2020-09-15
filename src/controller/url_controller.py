from flask_restful import Resource, reqparse
from models.url import Url	

class UrlController(Resource):
    @staticmethod
    def __makeDeleteParser():
        deleteParser = reqparse.RequestParser()
        deleteParser.add_argument('id',
           type=int,
           required=True,
           help="This is a required field."
        )
        return deleteParser

    @staticmethod
    def __makeGetParser():
        getParser = reqparse.RequestParser()
        getParser.add_argument('keywords',
           type=int,
           required=True,
           help="This is a required field."
        )
        return getParser

    __deleteParser = __makeDeleteParser.__func__()
    __getParser = __makeGetParser.__func__()

    def delete(self):
        inputData = UrlController.__deleteParser.parse_args()
        url = Url.find_url_by_id(inputData['id'])
        url.deleteUrl()

        return {"message": "Posting deleted Successfully."}, 201

    def get(self):
        inputData = UrlController.__getParser.parse_args()
	
        return {'urls': list(map(lambda x: x.json(), 
                Url.find_url_by_keywords(inputData['keywords'])))}