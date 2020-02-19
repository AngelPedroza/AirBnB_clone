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
