#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

#from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
#from datetime import datetime
import json
import os
#import re
#import time
#import unittest
import uuid
import unittest

class Test_base(unittest.TestCase):

    """Unittest for BaseModels."""

    def setUp(self):
        """Sets up methods"""
        pass

    def tearDown(self):
        """ reset file.json """
        try:
            remove("file.json")
        except:
            pass

    def test_task_3(self):
        """Tests instances in BaseModel"""

        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_no_args(self):
        """ test without arguments """
        with self.assertRaises(TypeError) as error:
            BaseModel.__init__()
        err = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), err)
