#!/usr/bin/python3

""" State creation """

from models.base_model import BaseModel


class State(BaseModel):
    """ State class
    Args:
        BaseModel : inheritance
    """
    name = str("")
