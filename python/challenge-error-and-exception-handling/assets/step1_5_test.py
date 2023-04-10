import sys

sys.path.append("/home/labex/project")

import unittest

from custom_exceptions_and_logging import process_data, InvalidDataError


class TestStep1(unittest.TestCase):
    def test_process_data_has_not_data(self):
        self.assertRaises(InvalidDataError, process_data, "")


if __name__ == "__main__":
    unittest.main()
