import unittest
import sys

sys.path.append("/home/labex/project")
from typing import List, Union, Dict
from count_data_types import count_data_types


class TestCountDataTypes(unittest.TestCase):
    def test_count_data_types(self):
        data = [
            1,
            2.5,
            "hello",
            True,
            [1, 2, 3],
            (1, 2, 3),
            {"a": 1, "b": 2},
            {1, 2, 3},
        ]
        result = count_data_types(data)
        self.assertEqual(
            result,
            {
                "int": 1,
                "float": 1,
                "str": 1,
                "bool": 1,
                "list": 1,
                "tuple": 1,
                "dict": 1,
                "set": 1,
            },
        )

        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = count_data_types(data)
        self.assertEqual(
            result,
            {
                "int": 10,
                "float": 0,
                "str": 0,
                "bool": 0,
                "list": 0,
                "tuple": 0,
                "dict": 0,
                "set": 0,
            },
        )

        data = [1.0, 2.5, 3.14, 4.2, 5.0]
        result = count_data_types(data)
        self.assertEqual(
            result,
            {
                "int": 0,
                "float": 5,
                "str": 0,
                "bool": 0,
                "list": 0,
                "tuple": 0,
                "dict": 0,
                "set": 0,
            },
        )

        data = ["hello", "world", "python", "unittest"]
        result = count_data_types(data)
        self.assertEqual(
            result,
            {
                "int": 0,
                "float": 0,
                "str": 4,
                "bool": 0,
                "list": 0,
                "tuple": 0,
                "dict": 0,
                "set": 0,
            },
        )


if __name__ == "__main__":
    unittest.main()
