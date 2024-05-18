#!/usr/bin/python3
from pathlib import Path
import json

class FileStorage:
    """save objectts in json on a file"""
    
    def __init__(self):
        self.__file_path = Path.cwd()
        self.__objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects.update({obj.__class__.__name__: obj.id})
        return self.__objects
    
    def save(self):
        with open("file.json", "w") as file:
            self.json_obj = json.dumps(self.__dict__, indent=6)
            file.write(self.json_obj)
    
    def reload(self):
        if Path.exists(self.__file_path):
            try:
                with open("file.json", "r") as file:
                    obj = json.load(file)
                    self.__objects.update({obj.__class__.__name__: obj.id})
            except:
                pass