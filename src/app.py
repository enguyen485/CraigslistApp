from db import db
from flask import Flask
from flask_restful import Api
from controller.url_controller import UrlController
from controller.detector_controller import DetectorController

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'Aw2dWr6'
    
    #Adding resources
    api = Api(app)
    api.add_resource(UrlController, '/Url')
    api.add_resource(DetectorController, '/Detector')

    db.app = app
    db.init_app(app)
    app.app_context().push()

    with app.app_context():
        db.create_all()
        DetectorController.initialize()
    
    app.run(port=5000, debug=True, use_reloader=False)