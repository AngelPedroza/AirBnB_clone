#!/usr/bin/python3
"""Module for save and read since a file"""
import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}
    DC = [
        "BaseModel", "User", "Place", "State",
        "City", "Amenity", "Review"
    ]

    def all(self):
        """Return the dict of a object"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            res = {}
            for key, value in FileStorage.__objects.items():
                res[key] = value.to_dict()
            f.write(json.dumps(res))

    def str_class(self):
        """ Classes to compare with line """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dict_class = {"BaseModel": BaseModel,
                      "User": User,
                      "Place": Place,
                      "State": State,
                      "City": City,
                      "Amenity": Amenity,
                      "Review": Review}
        return dict_class

    def reload(self):
        """ Deserializes JSON file """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        if os.path.isfile(FileStorage.__file_path) is True:
            dict_class = {
                "BaseModel": BaseModel, "User": User,
                "Place": Place, "State": State,
                "City": City, "Amenity": Amenity,
                "Review": Review
            }

            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj = json.loads(f.read())
                for key, value in obj.items():
                    obj = dict_class[value["__class__"]](**value)
                    key_obj = value["__class__"] + "." + value["id"]
                    FileStorage.__objects[key_obj] = obj

    def create(self, key):
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dict_class = {
            "BaseModel": BaseModel, "User": User,
            "Place": Place, "State": State,
            "City": City, "Amenity": Amenity,
            "Review": Review
        }

        obj = dict_class[key]()
        self.new(obj)
        self.save()
        return obj.id
