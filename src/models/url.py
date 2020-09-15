from db import db
from typing import Dict, Optional, List

class Url(db.Model):
    """
    Represents a url that corresponds to a new listing on craigslist\n
    Fields:\n
    id --> url ID. Unique to every url.\n
    hyperlink --> The hyperlink that corresponds to a specific listing
    keywords --> The keywords that match this new listing
    data --> The date that this listing was found
    @author ericnguyen
    """
    
    __tablename__ = 'URLs'
    id = db.Column(db.Integer, primary_key=True)
    hyperlink = db.Column(db.String, unique=False, nullable=False)
    keywords = db.Column(db.Integer, nullable=False, default=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return "Listing ID: %s, keywords: %s" % (self.id, self.keywords)

    def __init__(self, hyperlink, keywords, is_deleted):
        self.hyperlink = hyperlink
        self.keywords = keywords
        self.is_deleted = is_deleted

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def json(self) -> Dict[str, str]:
        ret = {}
        ret['id'] = self.id
        ret['hyperlink'] = self.hyperlink
        ret['keywords'] = self.keywords
        ret['is_deleted'] = self.is_deleted
        return ret

    @staticmethod
    def get_all_urls():
        return Url.query.all()

    @staticmethod
    def find_url_by_id(id: int):
        '''
        Finds an url in the database based on its id.\n
        Params:\n
        id--> The id associated with a url\n
        Returns:\n
        Returns an url with the corresponding id\n
        '''
        return Url.query.filter_by(id=id).first()

    @staticmethod
    def find_url_by_hyperlink(hyperlink: str, keywords: int):
        '''
        Finds an url in the database based on its hyperlink.\n
        Params:\n
        hyperlink --> The hyperlink associated with a url\n
        Returns:\n
        Returns an url with the corresponding hyperlink\n
        '''
        return Url.query.filter_by(hyperlink=hyperlink, keywords=keywords).first()

    @staticmethod
    def find_url_by_keywords(keywords: int):
        '''
        Finds all urls with the given keywords search.\n
        Params:\n
        keywords --> The id of a specific url\n
        Returns:\n
        Returns all url with the corresponding keyword\n
        '''
        return Url.query.filter_by(keywords=keywords, is_deleted = False).all()

    def deleteUrl(self):
        self.is_deleted = True
        self.save()

    
