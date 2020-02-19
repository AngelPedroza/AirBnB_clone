#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
import time
import uuid
import unittest

class Test_storage(unittest.TestCase):

    """Unittest for FileStorage"""

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

    def test_task_5_instantiation(self):
        """ test storage class """
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_task5_attrs(self):
        """ test attributes of the class """
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage,"_FileStorage__objects"), {})

    def test_task5_all(self):
        """ test method save without arguments """
        with self.assertRaises(TypeError) as error:
            FileStorage.all(self, "Gabi")
        err = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), err)
