#!/usr/bin/python3

"""Defining a class User"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class representing a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
