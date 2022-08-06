#!/usr/bin/python3
import unittest
import uuid
from models import base_models

class Test_Base_Models(unittest.TestCase):
  """Unit test for testing instantiation of the BaseModel"""

  def test_id(self):
    """Testing for the id generation"""
    B1 = BaseModel()
    self.assertEqual(B1.id, uuid.uuid4())

  def unique_id(self):
    """Tests for unique id"""
    B1 = Basemodel()
    B2 = BaseModel()
    self.assert(B1.id is not B2.id)
    
  def type_id(self):
    self.assertRaises(TypeError, type(B1.id), )

  def update_time(self):
    self.assertEqual()
