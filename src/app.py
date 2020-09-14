import asyncio
from flask import Flask
from flask_restful import Api

from controller.urlController import Urls
from controller.searchController import Searches


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'eric'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#Adding resources
api.add_resource(Urls, '/Url')
api.add_resource(Searches, '/Search')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

    
    
