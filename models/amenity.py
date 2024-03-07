#!/usr/bin/python3

""" Amenity creation """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class
    Args:
        BaseModel : inheritance
    """
    name = str("")
