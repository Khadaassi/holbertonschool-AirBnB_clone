from models.base_model import BaseModel
from models.user import User
import unittest
import json
import datetime


class TestUser(unittest.TestCase):
    """Test User class implementation"""

    def test_class(self):
        """Validate the types of the attributes an class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)
