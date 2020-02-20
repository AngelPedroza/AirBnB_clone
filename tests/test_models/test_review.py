#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import time
import uuid
import unittest


class Test_ReviewInstance(unittest.TestCase):

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
        base = Review()
        self.assertEqual(str(type(base)),
                         "<class 'models.review.Review'>")
        self.assertIsInstance(base, Review)
        self.assertTrue(issubclass(type(base), Review))

class Test_ReviewAttr(unittest.TestCase):
    """Check the values of the attributes"""

    def test_valuesAttr(self):
        dic = {"text": "Hola perrito"}

        r = Review(**dic)
        self.assertEqual(type(r.place_id), str)
        self.assertEqual(type(r.user_id), str)
        self.assertEqual(type(r.text), str)
