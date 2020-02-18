#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

#from models import storage
#from models.base_model import BaseModel
#from models.engine.file_storage import FileStorage
#from datetime import datetime
#import json
#import os
#import re
#import time
#import unittest
#import uuid


class Test_base(unittest.TestCase):

    """Unittest for BaseModels."""

    def setUp(self):
        """Sets up methods"""
        pass

    def kill(self):
        """kill methods"""
        self.reset_file()
        pass

    def reset_file(self):
        """Reset file.json"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_task_3(self):
        """Tests instances in BaseModel"""

        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))
