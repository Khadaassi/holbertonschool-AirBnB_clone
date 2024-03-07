#!/usr/bin/python3

""" City creation """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class
    Args:
        BaseModel : inheritance
    """
    state_id = str("")
    name = str("")
