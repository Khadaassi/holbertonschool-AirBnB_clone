#!/usr/bin/python3

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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
            for obj in objs.values():
                cls = obj["__class__"]
                if cls in globals():
                    FileStorage.__objects[obj["id"]] = globals()[cls](**obj)
