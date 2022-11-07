#!/usr/bin/python3

"""Defining a class Review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """a class for reviews"""
    place_id = ""
    user_id = ""
    text = ""
