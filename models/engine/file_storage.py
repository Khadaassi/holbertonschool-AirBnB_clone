#!/usr/bin/python3

"""
This module contains the FileStorage class
"""

import json
import os


class FileStorage:
    """
    Represents a FileStorage class
    Attributes:
        __file_path (str): path to JSON file
        __objects (dict): dictionary of objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, getattr(obj, "id"))
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    instance = class_(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
