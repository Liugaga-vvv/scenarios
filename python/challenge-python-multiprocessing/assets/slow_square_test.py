import sys

sys.path.append("/home/labex/project")

from slow_square import slow_square
import multiprocessing
import unittest

class TestMultiprocessing(unittest.TestCase):
    def test_slow_square(self):
        pool = multiprocessing.Pool(processes=4)
        results = [pool.apply_async(slow_square, (x,)) for x in range(10)]
        for result in results:
            self.assertEqual(result.get(), result.get())
        pool.close()
        pool.join()

if __name__ == '__main__':
    unittest.main()
