#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import subprocess


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.storage = FileStorage()
    
    

if __name__ == '__main__':
    unittest.main()
