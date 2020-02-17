#!/usr/bin/python3
""" modules for class basemodel """

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Class baseModel """

    def __init__(self, *args, **kwargs):
        """ init if base instance """
        for key, value in kwargs.items():
            if key == "created_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

            if key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

            if key == "__class__":
                continue
            else:
                setattr(self, key, value)

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string of all atributtes of a instace"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    # Public instance methods
    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        str_dict = self.__dict__.copy()
        str_dict["__class__"] = self.__class__.__name__
        str_dict["created_at"] = self.created_at.isoformat()
        str_dict["updated_at"] = self.updated_at.isoformat()
        return str_dict
