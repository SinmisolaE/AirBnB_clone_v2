#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import base_declarative()


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), nullable=False, ForeignKey("places.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    text = Column(String(1024), nullable=False)
