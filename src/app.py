from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from controller.url_controller import Urls
from controller.detector_controller import DetectorController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Aw2dWr6'
api = Api(app)
    
#Adding resources
api.add_resource(Urls, '/Url')
api.add_resource(DetectorController, '/Detector')

if __name__ == '__main__':
    from db import db
    db.app = app
    app.app_context().push()
    db.init_app(app)
    with app.app_context():
        db.create_all()
        DetectorController.initialize()
    
    app.run(port=5000, debug=True, use_reloader=False)