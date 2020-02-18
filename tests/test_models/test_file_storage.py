"""Test file for BaseModel Class"""

import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class Test_Storage(unittest.TestCase):
    """ Test for file storage """

    def test_dictionary(self):
        storage = FileStorage()
        filedict = storage.all()
        self.assertIsInstance(filedict, dict)

    def test_objects(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_filepath(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_docstring(self):
        self.assertIsNotNone(FileStorage.__doc__)


if __name__ == '__main__':
    unittest.main()
