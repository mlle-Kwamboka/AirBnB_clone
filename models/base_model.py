#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
  """Class defining all common attributes and methods for other classes"""
  
  def __init__(self, *args, **kwargs):
      """Initializing BaseModel object
      """
      from models import storage
      
      if not kwargs:
          self.id = str(uuid.uuid4())
          self.created_at = self.updated_at = datetime.now()
          storage.new(self)
      else:
          for key, value in kwargs.items():
              if key != '__clas__':
                  if key in ('created_at', 'updated_at'):
                      setattr(self, key, datetime.fromisoformat(value))
                  else:
                      setattr(self, key, value)

  def __str__(self):
      """Returns a string representation in the format [BaseModel], (self.id), self.__dict__"""
    
      return [{}] ({}) {}.format(type(self).__name__, self.id, self.__dict__
    
  def save(self):
      """Updates the updated_at attribute with the current time"""
                                 
      from models import storage
      self.updated_at = datetime.now()
      storage.save()
    
  def to_dict(self):
      """returns dictionary representation of class attributes"""
      dict_1 = self.__dict__.copy()
      dict_1["__class__"] = self.__class__.__name__
      for k, v in self.__dict__.items():
          if k in ("created_at", "updated_at"):
              v = self.__dict__[k].isoformat()
              dict_1[k] = v
      return dict_1
     
