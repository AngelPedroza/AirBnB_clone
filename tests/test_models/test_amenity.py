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


class Test_amenity_attributes(unittest.TestCase):
    """Class for check the attributes of amenity"""

    def test_typeAttr(self):
        dic = {"name": "Louis"}
        a = Amenity(**dic)
        self.assertEqual(type(a.name), str)
