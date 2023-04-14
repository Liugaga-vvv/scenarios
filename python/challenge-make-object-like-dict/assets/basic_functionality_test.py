import sys

sys.path.append("/home/labex/project")

import unittest
from basic_functionality import DictLikeObject


class TestDictLikeObject(unittest.TestCase):
    def test_basic_functionality(self):
        # Test initialization
        d = DictLikeObject()
        self.assertEqual(len(d), 0)

        # Test setting and getting values
        d["key1"] = "value1"
        self.assertEqual(d["key1"], "value1")

        # Test removing key-value pairs
        del d["key1"]
        try:
            d["key1"]
        except KeyError as e:
            pass

        # Test raising KeyError when getting, setting, and deleting nonexistent keys
        with self.assertRaises(KeyError):
            d["key1"]
        with self.assertRaises(KeyError):
            del d["key1"]


if __name__ == "__main__":
    unittest.main()
