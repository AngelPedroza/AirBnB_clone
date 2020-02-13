#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """ Class baseModel """

    def __init__(self, *args, **kwargs):
        """ init if base instance """
        if len(kwargs) is not 0:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs[key]
                if key == "name":
                    self.name = kwargs[key]
                if key == "my_number":
                    self.my_number = kwargs[key]
                if key == "created_at":
                    val = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = val
                if key == "updated_at":
                    val = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return a string of all atributtes of a instace"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id,
                                     self.__dict__)

    #Public instance methods
    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        str_dict = self.__dict__.copy()
        str_dict["__class__"] = type(self).__name__
        str_dict["created_at"] = self.created_at.isoformat()
        str_dict["updated_at"] = self.updated_at.isoformat()
        return str_dict
