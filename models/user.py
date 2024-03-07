#!/usr/bin/python3
""" User creation """

from models.base_model import BaseModel


class User(BaseModel):
    """User class
    Args:
        BaseModel : inheritance
    """
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
