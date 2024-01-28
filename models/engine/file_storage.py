#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os

class FileStorage:
    # private class attributes
    __file_path = "file.json"
    __objects = {} # this is where you store the objects when it's not in the file storage. you also pull the objects into this place when you want to use it

    def all(self):
        return FileStorage.__objects # returns all the objects in the file
    
    def new(self, obj):
        rep = obj.to_dict()["__class__"] # get the class of the object
        the_id = obj.id # extract the id of the object
        obj_key = f"{rep}.{the_id}" # create a string containing the new key
        new  = {obj_key: obj} #make the string the key of the object
        self.all().update(new) #update the new data
    
    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            obj = {} # initialize an empty dictionary
            obj.update(FileStorage.__objects) # copy the content in the objects into the dictionary
            for key, value in obj.items():
                if isinstance(value, BaseModel): # if the object is an istance of BaseModel,
                    obj[key] = value.to_dict() # convert that object value to another dictionary
            json.dump(obj, f) # then dump the object into the file
    
    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj_string = json.load(f) # load the content of the json file into a variable
                for key, value in obj_string.items():
                    class_name, obj_id = key.split(".") # split the key into class name and id because thats howit was saved
                    cls = eval(class_name) # evaluate to ensure that the class actually exists in your program
                    obj = cls(**value) # if it exists, make it a key for the values associateed with it
                    self.new(obj) # make it an addition to the object file


