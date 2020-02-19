#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.user import User
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

    def test_task8(self):
        """ test instantiatione in the user class """
        base = User()
        self.assertEqual(str(type(base)),
                         "<class 'models.user.User'>")
        self.assertIsInstance(base, User)
        self.assertTrue(issubclass(type(base), User))
