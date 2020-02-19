#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

#from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import os
#import re
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

    def test_la_re_arguments(self):
        args = []
        for i in range(10000):
            args.append(i)
        base = BaseModel(1, 2, 3)
        base = BaseModel(*args)

    def test_task3_id(self):
        """ test for unique ids """
        length = [BaseModel().id for i in range(10000)]
        self.assertEqual(len(set(length)), len(length))

    def test_to_dict(self):
        """ test method to dict """
        base = BaseModel()
        base.name = "Maicol"
        base.age = 22
        convert = base.to_dict()
        self.assertEqual(convert["id"], base.id)
        self.assertEqual(convert["name"], base.name)
        self.assertEqual(convert["age"], base.age)
        self.assertEqual(convert["updated_at"], base.updated_at.isoformat())
        self.assertEqual(convert["created_at"], base.created_at.isoformat())
        self.assertEqual(convert["__class__"], type(base).__name__)

    def test_no_to_dict(self):
        """ try in empty to_dict """
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict()
        err = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), err)

    def test_task3_save(self):
        """ test for save method """
        base = BaseModel()
        time.sleep(0.05)
        now = datetime.now()
        base.save()
        interval = now - base.updated_at
        self.assertTrue(abs(interval.total_seconds()) < 0.01)

    def test_moreargs_to_dict(self):
        """ try more arguments for  to_dict """
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict(self, "striker")
        err = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), err)

    def test_task3_datetime(self):
        """ test for updated at and created at """
        now = datetime.now()
        base = BaseModel()
        interval = now - base.created_at
        self.assertTrue(abs(interval.total_seconds()) < 0.1)
        interval = now - base.updated_at
        self.assertTrue(abs(interval.total_seconds()) < 0.01)
