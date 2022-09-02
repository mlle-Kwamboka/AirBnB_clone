#!/usr/bin/python3
import unittest
from uuid import uuid4
import models
from models.base_model import BaseModel
from datetime import datetime
import os


class Test_Base_Models(unittest.TestCase):
    """Unit test for testing instantiation of the BaseModel"""

    def test_id(self):
        """Testing for the presence instance id """
        B = BaseModel()
        self.assertTrue(hasattr(B, "id"))

    def str_rep(self):
        """Tests that str representation is appropriate"""
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def unique_id(self):
        """Tests for unique id"""
        B1 = Basemodel()
        B2 = BaseModel()
        self.assertNotEqual(B1.id, B2.id)
        
    def type_id(self):
        """Tests that id is str"""
        B = BaseModel()
        self.assertTrue(Type(B.id) is str)
        
    def created_at_is_datetime(self):
        """Tests that created_at is datetime"""
        B = BaseModel()
        self.assertTrue(type(B.created_at) is datetime)

    def updated_at_is_datetime(self):
        """Tests that updated_at is datetime"""
        B = BaseModel()
        self.assertTrue(type(B.updated_at) is datetime)
