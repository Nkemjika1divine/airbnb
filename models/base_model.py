#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime


Base = declarative_base()


class BaseModel:
    def __init__(self, *args, **kwargs):
        from models.__init__ import storage # this is to avoid circular imports dangerous for programs
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue #skip if the key is a class name
                elif key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")) # create a dictionary of dictionaries
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print the name of the class, id and dctionary representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        from models.__init__ import storage
        """updates the current time at updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict_obj = self.__dict__.copy() # copy the dictionary
        dict_obj["__class__"] = self.__class__.__name__ # copy the name out and mskes it a key
        dict_obj['created_at'] = self.created_at.isoformat() # makes created_at a key
        dict_obj['updated_at'] = self.updated_at.isoformat() # makes updated_at a key
        return dict_obj
