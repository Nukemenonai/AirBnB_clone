#!/usr/bin/python3
"""
file storage module
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

objs = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review}


class FileStorage:
    """
    Serializes instances to a JSON file
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets obj in __objects"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ serializes to JSON """
        dummy_dict = {}
        for key, value in self.__objects.items():
            dummy_dict[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dummy_dict, f)

    def reload(self):
        """ deserializes JSON file to __objects"""
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                json_objs = json.load(f)
                for key in json_objs:
                    inst = objs[json_objs[key]['__class__']]
                    self.__objects[key] = inst(**(json_objs[key]))
