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
            pass

    def kill(self):
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """ reset file.json """
        self.kill()
        pass

    def test_task_5_instantiation(self):
        """ test storage class """
        self.kill()
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_task5_attrs(self):
        """ test attributes of the class """
        self.kill()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def test_task5_all(self):
        """ test method save without arguments """
        self.kill()
        with self.assertRaises(TypeError) as error:
            FileStorage.all(self, "Gabi")
        err = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), err)

    def test_no_args(self):
        """ test method save without arguments """
        self.kill()
        with self.assertRaises(TypeError) as error:
            FileStorage.__init__()
        err = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(error.exception), err)

    def test_more_args(self):
        """ test method save without arguments """
        self.kill()
        with self.assertRaises(TypeError) as error:
            base = FileStorage(1, 2, 3, 4)
        err = "object() takes no parameters"
        self.assertEqual(str(error.exception), err)

    def test_all_BaseModel(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["BaseModel"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_City(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["City"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_Review(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["Review"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_Place(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["Place"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_Amenity(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["Amenity"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_User(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["User"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)

    def test_all_State(self):
        """ test for all() method in all classnames """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        obj= storage.tester()["State"]()
        storage.new(obj)
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], obj)


    def test_re_objs_BaseModel(self):
        """ test for all() method in all classnames with many objects """
        self.kill()
        self.assertEqual(storage.all(), {}) # check that file.json is empty
        cl = storage.tester()["BaseModel"]
        objs = [cl() for i in range(7000)]
        [storage.new(obj) for obj in objs]
        self.assertEqual(len(objs), len(storage.all())) # check if
                                                        # create 7000 objs
        for obj in objs:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], obj)

if __name__ == "__main__":
    unittest.main()
