from db import db
from typing import Dict, Optional, List


class Url(db.Model):
    """
    Represents a url that corresponds to a new listing on craigslist\n
    Fields:\n
    id --> url ID. Unique to every url.\n
    hyperlink --> The hyperlink that corresponds to a specific listing
    craigslist_id --> The id number of the listing that craigslist has assigned
    keywords --> The keywords that match this new listing
    data --> The date that this listing was found
    @author ericnguyen
    """

    __tablename__ = 'URLs'
    id = db.Column(db.Integer, primary_key=True)
    hyperlink = db.Column(db.String, unique=False, nullable=False)
    craigslist_id = db.Column(db.Integer, nullable=False, default=False)
    keywords = db.Column(db.Integer, nullable=False, default=False)
    date = db.Column(db.String, nullable=False, default=False)

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self) -> str:
        return "Listing ID: %s, keywords: %s" % (self.id, self.keywords)

    def __init__(self, hyperlink, craigslist_id, keywords, date):
        self.hyperlink = hyperlink
        self.craigslist_id = craigslist_id
        self.keywords = keywords
        self.date = date

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def json(self) -> Dict[str, str]:
        ret = {}
        ret['id'] = self.id
        ret['hyperlink'] = self.hyperlink
        ret['craigslist_id'] = self.craigslist_id
        ret['keywords'] = self.keywords
        ret['date'] = self.date
        return ret

    @staticmethod
    def find_url_by_id(craigslist_id: int, keywords: int):
        '''
        Finds an url in the database based on its id.\n
        Params:\n
        craigslist_id --> The id of a specific url\n
        keywords --> The foreign key associated with the keyword search\n
        Returns:\n
        Returns an url with the corresponding id\n
        '''
        return Url.query.filter_by(craigslist_id=craigslist_id, keywords=keywords).first()

    @staticmethod
    def find_url_by_keywords(keywords: int):
        '''
        Finds all urls with the given keywords search.\n
        Params:\n
        keywords --> The id of a specific url\n
        Returns:\n
        Returns all url with the corresponding keyword\n
        '''
        return Url.query.filter_by(keywords=keywords).all()
