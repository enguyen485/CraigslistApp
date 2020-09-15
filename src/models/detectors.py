from db import db
from typing import Dict, Optional, List

class Detector(db.Model):
    """
    Represents detector that a user wants to be notified for\n
    Fields:\n
    id --> url ID. Unique to every detector.\n
    keywords --> The keywords that the user is detectoring for\n
    min_price --> The minimum price that is associated with this detector\n
    max_price --> The maximum price that is associated with this detector\n
    @author ericnguyen
    """
    __tablename__ = 'Detectors'
    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.String, unique=True, nullable=False)
    min_price = db.Column(db.Integer, nullable=False)
    max_price = db.Column(db.Integer, nullable=False)

    def __init__(self, keywords, min_price, max_price):
        self.keywords = keywords
        self.min_price = min_price
        self.max_price = max_price

    def __repr__(self) -> str:
        return "Keywords: %s, Min Price: %d, Max Price: %d" % (self.keywords, self.min_price, self.max_price)

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def json(self) -> Dict[str, str]:
        ret = {}
        ret['id'] = self.id
        ret['keywords'] = self.keywords
        ret['min_price'] = self.min_price
        ret['max_price'] = self.max_price
        return ret

    '''
    Finds all detectors stored in the database.\n
    Params:\n
    None\n
    Returns:\n
    Returns all the detectors\n
    '''
    @staticmethod
    def get_all_detectors():
        return Detector.query.filter_by().all()
    
    '''
    Finds all detectors stored in the database.\n
    Params:\n
    None\n
    Returns:\n
    Returns all the detectors\n
    '''
    @staticmethod
    def get_detectors_by_keywords(keywords: str):
        return Detector.query.filter_by(keywords=keywords).first()