#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.review import Review
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage


if (getenv("HBNB_TYPE_STORAGE") == "db"):
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
