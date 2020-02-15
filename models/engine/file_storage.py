#!/usr/bin/python3
"""Module for save and read since a file"""
import json
import os

class FileStorage:

    __file_path = "file.json"
    __objects = {}

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

    def reload(self):
        """ Deserializes JSON file """
        from models.base_model import BaseModel

        if os.path.isfile(FileStorage.__file_path) is True:
            dict_class = {"BaseModel": BaseModel}

            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj = json.loads(f.read())
                for key, value in obj.items():
                    self.new(dict_class[value["__class__"]](**value))
