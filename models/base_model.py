#!/usr/bin/python3

""" Base model class for AirBnB clone """

import uuid
from datetime import datetime


class BaseModel:
    """Base class for AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize class instance"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            from models import f_storage
            f_storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        from models import f_storage
        f_storage.new(self)
        f_storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
