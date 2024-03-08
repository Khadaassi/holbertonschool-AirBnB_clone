#!/usr/bin/python3
""" Unit tests for the FileStorage class """

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest
import json


class TestFileStorage(unittest.TestCase):
    """Test class for the FileStorage class"""

    def test_file_path(self):
        """Test file path"""
        model = BaseModel()
        model.save()
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        os.remove("file.json")

    def test_objects_dict(self):
        """Test objects dictionary"""
        model = BaseModel()
        model.save()
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        os.remove("file.json")

    def test_all(self):
        """Test all filestorage"""
        storage = FileStorage()
        instance = storage.all()
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, dict)

    def test_new(self):
        """Test new filestorage"""
        FileStorage._FileStorage__objects = {}
        objects = FileStorage._FileStorage__objects
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEqual(objects[f"{model.__class__.__name__}.{model.id}"], None)

    def test_save(self):
        """Test save filestorage"""
        bm = BaseModel()
        storage = FileStorage()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel." + bm.id, file.read())
        os.remove("file.json")

    def test_reload(self):
        """Test reload filestorage"""
        bm = BaseModel()
        storage = FileStorage()
        storage.new(bm)
        storage.save()
        storage.reload()
        FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, FileStorage._FileStorage__objects)
        os.remove("file.json")

    def test_init(self):
        """Test instance init"""
        file = FileStorage()
        self.assertIsInstance(file._FileStorage__objects, dict)
        self.assertIsInstance(file._FileStorage__file_path, str)

    def test_reload2(self):
        """Test reload filestorage"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_reload3(self):
        """Test reload filestorage"""
        test_dict = {
            "BaseModel.test": {
                "id": "test",
                "created_at": "2023-10-23T14:10:06.000000",
                "updated_at": "2023-10-23T14:10:06.000000",
                "__class__": "BaseModel",
            }
        }

        with open(FileStorage._FileStorage__file_path, "w") as file:
            json.dump(test_dict, file)

        storage = FileStorage()
        storage.reload()

        loaded_obj = storage.all()["BaseModel.test"]
        self.assertIsInstance(loaded_obj, BaseModel)
        self.assertEqual(loaded_obj.id, "test")
        self.assertEqual(str(loaded_obj.created_at), "2023-10-23 14:10:06")
        self.assertEqual(str(loaded_obj.updated_at), "2023-10-23 14:10:06")

        os.remove(FileStorage._FileStorage__file_path)
