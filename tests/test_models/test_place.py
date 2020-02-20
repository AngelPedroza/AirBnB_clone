#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import time
import uuid
import unittest


class Test_base(unittest.TestCase):

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
        """ test instantiatione in the place class """
        base = Place()
        self.assertEqual(str(type(base)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(base, Place)
        self.assertTrue(issubclass(type(base), Place))

class Test_allAttr(unittest.TestCase):
    """Test the type and more of each attribute of city"""

    def test_types(self):
        """Test teh correct types before setit"""
        dic = {
            "name": "Bogota", "description": "masa", "number_rooms": 4,
            "number_bathrooms": 2, "max_guest": 4, "price_by_night": 4000,
            "latitude": 2.5, "longitude": 1.5
        }
        c = Place(**dic)
        self.assertEqual(type(c.name), str)
        self.assertEqual(type(c.description), str)
        self.assertEqual(type(c.number_rooms), int)
        self.assertEqual(type(c.number_bathrooms), int)
        self.assertEqual(type(c.max_guest), int)
        self.assertEqual(type(c.price_by_night), int)
        self.assertEqual(type(c.latitude), float)
        self.assertEqual(type(c.longitude), float)
        self.assertEqual(type(c.city_id), str)
        self.assertEqual(type(c.user_id), str)
        self.assertEqual(type(c.amenity_ids), str)
