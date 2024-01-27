#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """print the name of the class, id and dctionary representation"""
        return "[{}] ({}) {}".format(self.__cls__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the current time at updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_obj = self.__dict__.copy() # copy the dictionary
        dict_obj["__class__"] = self.__class__.__name__ # copy the name out and mskes it a key
        dict_obj['created_at'] = self.created_at.isoformat() # makes created_at a key
        dict_obj['updated_at'] = self.updated_at.isoformat() # makes updated_at a key
