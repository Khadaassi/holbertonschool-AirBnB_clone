import unittest
from models.state import State


class test_state(unittest.TestCase):
	def test_state(self):
		"""Tests the value of the name attribute of the State class"""
		self.assertEqual(State.name, "")
