import sys

sys.path.append("/home/labex/project")
import unittest
from elapsed_time import elapsed_time


class TestElapsedTime(unittest.TestCase):
    def test_elapsed_time(self):
        self.assertEqual(elapsed_time("2022-01-01", "2022-01-31"), 30)
        self.assertEqual(elapsed_time("2022-02-01", "2022-02-10"), 9)
        self.assertEqual(elapsed_time("2022-03-01", "2022-03-31"), 30)


if __name__ == "__main__":
    unittest.main()
