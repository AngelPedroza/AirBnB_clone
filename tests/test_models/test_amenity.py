#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import time
import uuid
import unittest


class Test_instanceAmenity(unittest.TestCase):

    """Unittest for BaseModels."""

    def setUp(self):
        """Sets up methods"""
        try:
            remove("file.json")
        except:
            pass
        FileStorage._FileStorage_objects = {}

    def tearDown(self):
        """ reset file.json """
        try:
            remove("file.json")
        except:
            pass

    def test_task9(self):
        """ test instantiatione in the user class """
        a = Amenity()
        self.assertEqual(str(type(a)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(a, Amenity)
        self.assertTrue(issubclass(type(a), Amenity))

    def test_isinstance_args(self):
        """Test if have a instance with args"""
        a = Amenity("Hello", 123, ["World"])
        self.assertIsInstance(a, Amenity)

    def test_isinstance_kwargs(self):
        dic ={"hola": "world"}
        a = Amenity(**dic)
        self.assertIsInstance(a, Amenity)

class Test_amenity_attributes(unittest.TestCase):
    """Class for check the attributes of amenity"""
    def tearDown(self):
        """ reset file.json """
        try:
            remove("file.json")
        except:
            pass

    def exist_attr(self):
        """Check if exist the correct att"""
        att = ["name"]
        a = Amenity()
        dic = a.__dict__
        self.assertTrue(att in dic)

    def set_attr(self):
        """Check the correct setting"""
        a = Amenity()
        key = ["name"]
        val = ["Maicol"]
        tup = tuple(key, val)
        setattr(a, tup[0], tup[1])
        self.assertEqual(getattr(a, tup[0], False), tup[1])

    def test_initAmenity_keys(self):
        """Check if amenity set good without more elements"""
        a = Amenity()
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))

    def test_initAmenity_values(self):
        """Check if the amneity set good the values"""
        a = Amenity()
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_kwargsPass(self):
        """Pass kwargs to the init"""
        kwargs = {"helo": "world", "number": 123}
        a = Amenity(**kwargs)
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "helo"))
        self.assertTrue(hasattr(a, "number"))

        self.assertEqual(getattr(a, "helo", False), "world")
        self.assertEqual(getattr(a, "number", False), 123)

    def test_typeNameAttr(self):
        """check the type of the attru=ibutes"""
        a = Amenity()
        setattr(a, "name", "Louis")
        self.assertIsInstance(type(a.name), str)

        setattr(a, "name", 2)
        self.assertIsInstance(type(a.name), str)

        setattr(a, "name", 2.0)
        self.assertIsInstance(type(a.name), str)
