#!/usr/bin/python3

"""Unittest for City class"""

import unittest
from models.city import City


class test_city(unittest.TestCase):
    def test_city(self):
        """Tests default values for City class attributes"""
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")
