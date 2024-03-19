#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import base_declarative()
import shlex
from sqlalchemy.orm import relationship
from models.review import Review
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphans', backref="place")
    else:
        @property
        def reviews(self):
            """ returns list of Review instances with place_id == Place.id"""
            dict = models.storage.all()
            result = {}
            for key in dict:
                name = key.replace('.', ' ')
                name = shlex.split(name)
                if (name[0] == "Review"):
                    if (dict[key].place_id == self.id):
                        result.append(dict[key])
            return result
