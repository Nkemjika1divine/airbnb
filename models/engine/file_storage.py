#!/usr/bin/python3
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects # returns all the objects in the file
    
    def new(self, obj):
        rep = obj.to_dict()["__class__"] # get the class of the object
        the_id = obj.id # extract the id of the object
        obj_key = f"{rep}.{the_id}" # create a string containing the new key
        new  = {obj_key: obj} #make the string the key of the object
        self.all().update(new) #update the new data