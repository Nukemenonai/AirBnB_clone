"""Test file for BaseModel Class"""

import unittest

from models.base_model import BaseModel
from datetime import datetime


class Test_Model(unittest.TestCase):
    """ Test for ModelBase """

    def test_instance(self):
        Base1 = BaseModel()
        Base2 = BaseModel()
        self.assertTrue(Base1.id != Base2.id)

    def test_change_id(self):
        Base1 = BaseModel()
        Base1.id = "Hola"
        self.assertEqual(Base1.id, "Hola")

    def test_change_crtm(self):
        Base1 = BaseModel()
        Base1.created_at = "2020-10-20"
        self.assertEqual(Base1.created_at, "2020-10-20")

    def test_change_uptm(self):
        Base1 = BaseModel()
        Base1.updated_at = "2020-11-20"
        self.assertEqual(Base1.updated_at, "2020-11-20")

    def test_change_id(self):
        Base1 = BaseModel()
        Base1.id = "Hola"
        self.assertEqual(Base1.id, "Hola")

    def test_isinstance(self):
        Base1 = BaseModel()
        self.assertIsInstance(Base1, BaseModel)

    def test_instance_arg(self):
        with self.assertRaises(TypeError):
            Base1 = BaseModel(12)

    def test_create(self):
        Base1 = BaseModel()
        self.assertTrue(Base1 is not None)

    def test_create_time(self):
        Base1 = BaseModel()
        self.assertTrue(Base1.created_at is not None)

    def test_update_time(self):
        Base1 = BaseModel()
        self.assertTrue(Base1.updated_at is not None)

    def test_take_create_time(self):
        Base1 = BaseModel()
        self.assertIsInstance(Base1.created_at, datetime)

    def test_take_update_time(self):
        Base1 = BaseModel()
        self.assertIsInstance(Base1.updated_at, datetime)

    def test_updated_time(self):
        Base1 = BaseModel()
        PrevTime = Base1.updated_at
        Base1.save()
        self.assertTrue(Base1.updated_at != PrevTime)

    def test_instanceofstr(self):
        Base1 = BaseModel()
        str1 = Base1.__str__()
        self.assertIsInstance(str1, str)

    def test_str(self):
        Base1 = BaseModel()
        sr = "[" + Base1.__class__.__name__ + "]"
        sr += " (" + str(Base1.id) + ") "
        sr += str(Base1.__dict__)
        self.assertEqual(Base1.__str__(), sr)

    def test_instanceofdict(self):
        Base1 = BaseModel()
        dict1 = Base1.to_dict()
        self.assertIsInstance(dict1, dict)

    def test_isoformatchange(self):
        Base1 = BaseModel()
        with self.assertRaises(AttributeError):
            Base1.created_at = "2020-10-20"
            Base1.to_dict()

    def test_str_isoformat_change(self):
        Base1 = BaseModel()
        Base1.created_at = "2020-10-20"
        self.assertTrue(Base1.__str__() is not None)

    def test_stringid(self):
        Base1 = BaseModel()
        self.assertIsInstance(Base1.id, str)

    def test_stringid(self):
        Base1 = BaseModel()
        self.assertIsInstance(Base1.id, str)

    def test_string_created_time(self):
        Base1 = BaseModel()
        Base1.to_dict()
        self.assertIsInstance(Base1.created_at, str)

    def test_string_updated_time(self):
        Base1 = BaseModel()
        Base1.to_dict()
        self.assertIsInstance(Base1.updated_at, str)


if __name__ == '__main__':
    unittest.main()
