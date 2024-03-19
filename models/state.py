#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declaratvie_base()
from sqlalchemy.orm import relationship
import models
from models.city import City
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan', backref="state")

    @property
    def cities(self):
        """ returns list of City instances with state_id == State.id"""
        list = {}
        result = {}
        vars = models.storage.all()
        for key in vars:
            name = key.replace('.', ' ')
            name = shlex.split(name)
            if name[0] == 'City':
                if vars[key].state_id == self.id:
                    result.append(vars[key])
        return result
