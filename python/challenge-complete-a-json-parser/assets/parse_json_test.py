import sys

sys.path.append("/home/labex/project")
from parse_json import *
import unittest


class TestParseJson(unittest.TestCase):
    def test_parse_object(self):
        json_str = '{"name": "John Smith", "age": 42, "isMarried": false}'
        obj = parse_json(json_str)
        self.assertEqual(obj, {"name": "John Smith", "age": 42, "isMarried": False})

    def test_parse_array(self):
        json_str = "[1, 2, 3]"
        obj = parse_json(json_str)
        self.assertEqual(obj, [1, 2, 3])

    def test_parse_string(self):
        json_str = '"Hello, world!"'
        obj = parse_json(json_str)
        self.assertEqual(obj, "Hello, world!")

    def test_parse_number(self):
        json_str = "42"
        obj = parse_json(json_str)
        self.assertEqual(obj, 42)

    def test_parse_boolean(self):
        json_str = "true"
        obj = parse_json(json_str)
        self.assertEqual(obj, True)

    def test_parse_null(self):
        json_str = "null"
        obj = parse_json(json_str)
        self.assertEqual(obj, None)


if __name__ == "__main__":
    unittest.main()
