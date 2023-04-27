import sys

sys.path.append("/home/labex/project")
import unittest
import numpy as np
from convert_to_dtype import convert_to_dtype


class TestConvertToDtype(unittest.TestCase):
    def test_int8(self):
        lst = [1, 2, 3, 4, 5]
        expected = np.array([1, 2, 3, 4, 5], dtype="int8")
        result = convert_to_dtype(lst, "int8")
        np.testing.assert_array_equal(result, expected)

    def test_float32(self):
        lst = [1, 2, 3, 4, 5]
        expected = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype="float32")
        result = convert_to_dtype(lst, "float32")
        np.testing.assert_array_equal(result, expected)

    def test_uint64(self):
        lst = [1, 2, 3, 4, 5]
        expected = np.array([1, 2, 3, 4, 5], dtype="uint64")
        result = convert_to_dtype(lst, "uint64")
        np.testing.assert_array_equal(result, expected)

    def test_empty_list(self):
        lst = []
        expected = np.array([], dtype="float64")
        result = convert_to_dtype(lst, "float64")
        np.testing.assert_array_equal(result, expected)

    def test_invalid_dtype(self):
        lst = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            result = convert_to_dtype(lst, "invalid_dtype")


if __name__ == "__main__":
    unittest.main()
