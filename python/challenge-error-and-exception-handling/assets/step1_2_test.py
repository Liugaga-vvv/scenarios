import sys

sys.path.append("/home/labex/project")

import unittest

from custom_exceptions_and_logging import read_data_from_file


class TestStep1(unittest.TestCase):
    def test_file_not_found_error_has_file(self):
        result = read_data_from_file("/home/labex/project/example.txt")
        self.assertEqual(result, "example content")


if __name__ == "__main__":
    unittest.main()
