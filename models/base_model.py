#!/usr/bin/python3
import uuid
from datetime import datetime
class BaseModel:
  """Class defining all common attributes and methods for other classes"""
  
  id = str(uuid.uuid4())
  created_at = (datetime.today())
  updated_at = (datetime.today())

  def __init__(self, id, name, created_at, updated_at):
    """Initializing BaseModel object
    args:
      id: The uuid of the instance
      name: the name of the object
      created_at: The time it was created
      updated_at: The time it was updated
    """
    self.id = id
    self.name = name
    self.created_at = created_at
    self.updated_at = updated_at

  def __str__(self):
    """Returns a string representation"""
    return ([BaseModel], (self.id), self.__dict__)
  def save(self):
    """Updates the updated_at attribute with the current time"""
    self.updated_at = datetime.now()
    return self.updated_at

  def to_dict(self):
    """returns dictionary representation of class attributes"""
    return {'id': self.id, 'name': 'My_first_model', 'created_at': self.created_at.isoformat(), 'updated_at': self.updated_at.isoformat()}
