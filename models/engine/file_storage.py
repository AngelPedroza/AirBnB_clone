#!/usr/bin/python3
"""MOdule for save and read since a file"""
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
        fl = FileStorage.__file_path
        obj_v = FileStorage.__objects
        my_dict = {key: obj_v[key].to_dict() for key in obj_v.keys()}
        json_file = json.dumps(my_dict)

        with open(fl, mode="a", encoding="utf-8") as fd:
            fd.write(json_file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path) is True:
            try:
                fl = FileStorage.__file_path
                with open(fl, mode="r", encoding="utf-8") as fd:
                    my_json = fd.read()
                my_dict = json.loads(my_json)
                for key in my_dict:
                    FileStorage.__objects[key] = my_dict[key]
            except:
                pass
