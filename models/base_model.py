#!/usr/bin/env python3
"""
Class BaseModel that defines the attributes and methods
for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ Class BaseModel that defines the attributes and methods
    for other classes """
    def __init__(self, *args, **kwargs):
        """Constructor for a Class"""

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

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
        new = datetime.now()
        setattr(self, 'updated_at', new)
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of an instance with a new key called '__class__'
        and specific format for datetime keys
        """
        new = {}
        _dict = self.__dict__
        for key in _dict:
            if key == 'created_at' or key == 'updated_at':
                new[key] = _dict[key].isoformat()
            else:
                new[key] = _dict[key]
        new['__class__'] = self.__class__.__name__
        return (new)
