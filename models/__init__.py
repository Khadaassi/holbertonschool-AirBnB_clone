#!/usr/bin/python3
""""""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

f_storage = FileStorage()
f_storage.reload()

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "Place": Place,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
    }
