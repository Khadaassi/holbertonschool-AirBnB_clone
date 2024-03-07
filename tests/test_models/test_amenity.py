#!/usr/bin/python3

""" Performs unit tests for the Amenity class """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def test_name_default(self):
        """Test the default name attribute"""
        self.assertEqual(self.amenity.name, "")

    def test_name_type(self):
        """Test the type of name"""
        self.assertIsInstance(self.amenity.name, str)
