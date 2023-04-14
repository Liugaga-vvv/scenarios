import sys

sys.path.append("/home/labex/project")

from square_multiprocessing import square_multiprocessing
import unittest

class TestSquareMultiprocessing(unittest.TestCase):
    def test_square_multiprocessing(self):
        integers = [1, 2, 3, 4, 5]
        expected_output = [1, 4, 9, 16, 25]
        self.assertEqual(square_multiprocessing(integers), expected_output)

    def test_square_multiprocessing_empty_list(self):
        integers = []
        expected_output = []
        self.assertEqual(square_multiprocessing(integers), expected_output)

    def test_square_multiprocessing_large_list(self):
        integers = list(range(100000))
        expected_output = [i*i for i in integers]
        self.assertEqual(square_multiprocessing(integers), expected_output)

if __name__ == '__main__':
    unittest.main()
