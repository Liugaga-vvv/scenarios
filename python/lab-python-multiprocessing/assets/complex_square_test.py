import sys

sys.path.append("/home/labex/project")

import unittest
import multiprocessing
from complex_square import square


class TestMultiprocessing(unittest.TestCase):
    def test_square(self):
        with multiprocessing.Pool(processes=4) as pool:
            results = pool.map(square, range(1000000))
        self.assertEqual(results[:10], [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])


if __name__ == "__main__":
    unittest.main()
