import sys

sys.path.append("/home/labex/project")

import unittest

from custom_exceptions_and_logging import read_data_from_file, FileNotFoundError


class TestStep1(unittest.TestCase):
    def test_file_not_found_error_has_not_file(self):
        self.assertRaises(
            FileNotFoundError, read_data_from_file, "on_existent_file.txt"
        )


if __name__ == "__main__":
    unittest.main()
