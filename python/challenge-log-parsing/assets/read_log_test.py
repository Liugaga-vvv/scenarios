import sys

sys.path.append("/home/labex/project")

import unittest
from read_log import read_log


class TestReadLog(unittest.TestCase):
    def test_read_log(self):
        try:
            file_name = "x.log"
            read_log(file_name)
        except Exception:
            self.assertRaises(FileNotFoundError)

        file_name = "access.log"
        self.assertEqual(read_log(file_name), 999)


if __name__ == "__main__":
    unittest.main()
