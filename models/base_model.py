#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """ contains common attributes """

    name = ""
    my_number = 0

    def __init__(self, *args, **kwargs):
        
        
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()#.isoformat()
            self.updated_at = datetime.now().isoformat()
        else:
            for self.key, self.value in kwargs.items():
                self.__dict__.update({self.key: self.value})

    def __str__(self):

        return "[{}] ({}) <{}>".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now().isoformat()
        storage.save()

    def to_dict(self):

        self.created_at = self.created_at.isoformat()
        self.__dict__ = dict([('my_number', self.my_number), ('name', self.name), ('__class__', self.__class__.__name__), ('updated_at', self.updated_at), ('id', self.id), ('created_at', self.created_at)])
        return self.__dict__