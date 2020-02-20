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


class Test_Userinstance(unittest.TestCase):

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

    def test_passArgs(self):
        """Pass args"""
        a = User("hello", 123, "world")
        self.assertIsInstance(a, BaseModel)

    def test_passKargs(self):
        """Pass a dict"""
        dic = {"hello": "world", "numbers": 123, "email": "reply@prouve.com"}
        a = User(**dic)
        self.assertTrue(hasattr(a, "hello"))
        self.assertTrue(hasattr(a, "numbers"))
        self.assertTrue(hasattr(a, "email"))

        self.assertEqual(getattr(a, "hello"), "world")
        self.assertEqual(getattr(a, "numbers"), 123)
        self.assertEqual(getattr(a, "email"), "reply@prouve.com")
        self.assertEqual(type(getattr(a, "email")), str)
        self.assertEqual(type(getattr(a, "password")), str)
        self.assertEqual(type(getattr(a, "first_name")), str)
        self.assertEqual(type(getattr(a, "last_name")), str)
