#!/usr/bin/python3
"""Unittest module for the amenity class"""

import unittest
import datetime import datetime
import time
from models.amenity import BaseModel
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_models import BaseModel

class TestBaseModel(unittest.TestCase):

    """Test Cases for the BaseModel class"""

    def setUp(self):
        """Sets up test methods"""
        pass

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets Filestorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of BaseModel class"""

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments"""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


    def test_3_init_many_args(self):
        """Tests __init__ with many arguments"""
        self.resetStorage()
        args = [i for i in range(1000)]
        b = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        b = BaseModel(*args)

    def test_3_attributes(self):
        """Test attributes value for instance of a BaseModel class."""

        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_3_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b = BaseModel()
        diff = b.updated_at - b.creaed_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_secons()) < 0.1)

    def test_3_id(self):
        """Tests for unique user ids"""

        l = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(1)), len(1))

    def test_3_save(self):
        """Tests the public instance method save()."""

        b = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

        def test_3_str(self):
            """Tests  for __str__ method"""
            b = BaseModel()
            rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
            rex = rex.match(str(b))
            self.assertIsNotNone(res)
            self.assertEqual(res.group(1), "BaseModel")
            self.assertEqual(res.group(2), b.id)
            s = res.group(3)
            s = res.sub
