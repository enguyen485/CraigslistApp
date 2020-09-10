from db import db
from typing import Dict, Optional, List


class Search(db.Model):
    """
    Represents searches that a user wants to be notified for\n
    Fields:\n
    id --> url ID. Unique to every search.\n
    keywords --> The keywords that the user is searching for\n
    min_price --> The minimum price that is associated with this search\n
    max_price --> The maximum price that is associated with this search\n
    @author ericnguyen
    """

    __tablename__ = 'Searches'
    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.String, unique=True, nullable=False)
    min_price = db.Column(db.Integer, nullable=False)
    max_price = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return "Keywords: %s, Min Price: %d, Max Price: %d" % (self.keywords, self.min_price, self.max_price)

    def __init__(self, keywords, min_price, max_price):
        self.keywords = keywords
        self.min_price = min_price
        self.max_price = max_price

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

    @staticmethod
    def find_searches_by_keywords(keywords: str):
        '''
        Finds a search based on the keywords entered.\n
        Params:\n
        keywords --> The keywords that a user is searching for\n
        Returns:\n
        Returns the search with the corresponding keywords\n
        '''
        return Search.query.filter_by(keywords=keywords).first()
