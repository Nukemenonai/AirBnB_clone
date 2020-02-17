"""
file storage module
"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets obj in __objects"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes to JSON """
        dummy_dict = {}
        for key, value in FileStorage.__objects.items():
            dummy_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dummy_dict, f)

    def reload(self):
        """ deserializes JSON file to __objects"""
        from models.base_model import BaseModel
        try:
            with open(FileStorage.__file_path) as f:
                json_objs = json.load(f)
                for key, value in json_objs.items():
                    inst = eval(value["__class__"] + '(**value)')
                    FileStorage.__objects[key] = inst
        except IOError:
            pass
