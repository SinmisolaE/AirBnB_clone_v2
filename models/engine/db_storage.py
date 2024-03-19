#!/usr/bin/python3
"""class DBStorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from sqlalchemy.ext.declarartve import declarative_base()
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City


class DBStorage:
    """ new engine for storage"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes attributes"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}/'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database all objects depending on class name"""
        dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for ins in query:
                key = "{}.{}".format(type(ins).__name__, ins.id)
                dict[key] = ins
        else:
            list = [State, Place, User, City, Amenity, Review]
            query = self.__session.query(list)
            for ins in query:
                key = "{}.{}".format(type(ins).__name__, ins.id)
                dict[key] = ins
        return dict

    def new(self, obj):
        """ adds object to current database session"""
        sef.__session.add(obj)

    def save(self):
        """commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in database"""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()
