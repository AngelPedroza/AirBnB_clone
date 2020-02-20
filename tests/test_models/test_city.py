#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import time
import uuid
import unittest


class Test_PlaceInstance(unittest.TestCase):
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

    def test_task8(self):
        """ test instantiatione in the user class """
        base = City()
        self.assertEqual(str(type(base)),
                         "<class 'models.city.City'>")
        self.assertIsInstance(base, City)
        self.assertTrue(issubclass(type(base), City))

class test_CityAttr(unittest.TestCase):
    """Check the type of attributes"""

    def test_typeAttr(self):
        """Come on"""
        dic = {"name": "San Francisco"}

        c = City(**dic)
        self.assertEqual(type(c.state_id), str)
        self.assertEqual(type(c.name), str)
