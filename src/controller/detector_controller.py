from flask_restful import Resource, reqparse
from models.detectors import Detector
from manager.detector_manager import DetectorManager
class DetectorController(Resource):
    def __init__(self):
        self.manager = DetectorManager.getInstance()
       
    @staticmethod
    def initialize():
        DetectorManager.getInstance().initialize()

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

        if Detector.get_detectors_by_keywords(inputData['keywords']):
            return {"message": "Detector already exists"}, 400

        detector = Detector(**inputData)
        detector.save()
        self.manager.addJob(detector, True)

        return {"message": "Detector added successfully."}, 201

    def get(self):
	
        return {"detectors": list(map(lambda x: x.json(), 
                Detector.get_all_detectors()))}

