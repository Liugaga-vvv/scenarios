import sys

sys.path.append("/home/labex/project")

import unittest


class TestStep1(unittest.TestCase):
    def test_find_exceptions(self):
        errs = []
        try:
            from custom_exceptions_and_logging import FileNotFoundError
        except ImportError as e:
            errs.append("FileNotFoundError")

        try:
            from custom_exceptions_and_logging import InvalidDataError
        except ImportError as e:
            errs.append("InvalidDataError")

        try:
            from custom_exceptions_and_logging import OperationFailedError
        except ImportError as e:
            errs.append("OperationFailedError")

        if len(errs) != 0:
            raise AssertionError(f"Custom exception not found: {', '.join(errs)}")


if __name__ == "__main__":
    unittest.main()
