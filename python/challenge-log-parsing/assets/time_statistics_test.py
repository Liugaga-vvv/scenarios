import sys

sys.path.append("/home/labex/project")

import unittest
from time_statistics import time_statistics


class TestTimeStatistics(unittest.TestCase):
    def test_time_statistics(self):
        try:
            file_name = "x.log"
            time_statistics(file_name)
        except Exception:
            self.assertRaises(FileNotFoundError)

        file_name = "access.log"
        max_uri, max_avg_time, min_uri, min_avg_time = time_statistics(file_name)
        self.assertEqual(max_uri, "/query/order/info")
        self.assertTrue(abs(max_avg_time - 1.54) < 0.01)

        self.assertEqual(min_uri, "/service/pricing")
        self.assertTrue(abs(min_avg_time - 1.33) < 0.01)


if __name__ == "__main__":
    unittest.main()
