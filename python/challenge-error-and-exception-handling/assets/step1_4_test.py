import sys

sys.path.append("/home/labex/project")

import unittest

from custom_exceptions_and_logging import process_data


class TestStep1(unittest.TestCase):
    def test_process_data_has_data(self):
        process_data("example content")


if __name__ == "__main__":
    unittest.main()
