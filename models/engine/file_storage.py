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

    def all(self, cls=None):
        """Return the dictionary __objects."""
        if cls is None:
            return self.__objects
        dict_storage = {}
        for key, value in self.__objects.items():
            if cls == value.__class__:
                dict_storage[key] = value
        return dict_storage

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        
    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, sort_keys=True, indent=4)
        
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
    classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """delete obj from __objects if its inside -
        if obj is equal to None, the method should
        not do anything"""
        if obj is not None:
            key_dict = obj.__class__.__name__ + '.' + obj.id
            if key_dict in self.__objects:
                del self.__objects[key_dict]

        
