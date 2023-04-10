import sys

sys.path.append("/home/labex/project")

from square import square
import multiprocessing
import unittest

class TestMultiprocessing(unittest.TestCase):
    def test_square(self):
        pool = multiprocessing.Pool(processes=4)
        results = pool.map(square, range(10))
        self.assertEqual(results, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

if __name__ == '__main__':
    unittest.main()
