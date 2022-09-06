#!/usr/bin/python3
"""Defines the FileStorage class."""
import json

class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        
