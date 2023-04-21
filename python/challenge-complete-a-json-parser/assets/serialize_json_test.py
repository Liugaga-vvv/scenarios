import sys

sys.path.append("/home/labex/project")
from serialize_json import *
import unittest


class TestSerializeJson(unittest.TestCase):
    def test_serialize_object(self):
        obj = {"name": "John Smith", "age": 42, "isMarried": False}
        json_str = serialize_json(obj)
        self.assertEqual(json_str, '{"name":"John Smith","age":42,"isMarried":false}')

    def test_serialize_array(self):
        obj = [1, 2, 3]
        json_str = serialize_json(obj)
        self.assertEqual(json_str, "[1,2,3]")

    def test_serialize_string(self):
        obj = "Hello, world!"
        json_str = serialize_json(obj)
        self.assertEqual(json_str, '"Hello, world!"')

    def test_serialize_number(self):
        obj = 42
        json_str = serialize_json(obj)
        self.assertEqual(json_str, "42")

    def test_serialize_boolean(self):
        obj = True
        json_str = serialize_json(obj)
        self.assertEqual(json_str, "true")

    def test_serialize_null(self):
        obj = None
        json_str = serialize_json(obj)
        self.assertEqual(json_str, "null")


if __name__ == "__main__":
    unittest.main()
