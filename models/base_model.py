#!/usr/bin/env python3
"""
Class BaseModel that defines the attributes and methods
for other classes
"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():

    def __init__(self, *args, **kwargs):
        """Constructor for a Class"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            storage.new(self)

    def __str__(self):
        """String representation of Object"""
        sr = "[" + self.__class__.__name__ + "]"
        sr += " (" + str(self.id) + ") "
        sr += str(self.__dict__)
        return (sr)

    def save(self):
        """
        Save into a file the Object converted in JSON String representation
        """
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """
        Returns a dictionary of an instance with a new key called '__class__'
        and specific format for datetime keys
        """
        key = "__class__"
        value = self.__class__.__name__
        self.__dict__[key] = value
        self.__dict__["created_at"] = self.__dict__["created_at"].isoformat()
        self.__dict__["updated_at"] = self.__dict__["updated_at"].isoformat()
        return (self.__dict__)
