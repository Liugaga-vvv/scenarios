import sys

sys.path.append("/home/labex/project")

import unittest
from advanced_functionality import DictLikeObject


class TestDictLikeObject(unittest.TestCase):
    def test_advanced_functionality(self):
        # Test membership testing
        d = DictLikeObject()
        d["key1"] = "value1"
        self.assertIn("key1", d)
        self.assertNotIn("key2", d)

        # Test iteration over keys
        d["key2"] = "value2"
        keys = []
        for key in d:
            keys.append(key)
        self.assertEqual(keys, ["key1", "key2"])

        # Test getting a list of keys
        self.assertEqual(d.keys(), ["key1", "key2"])


if __name__ == "__main__":
    unittest.main()
