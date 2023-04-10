import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch

from custom_exceptions_and_logging import (
    read_data_from_file,
    process_data,
    FileNotFoundError,
    InvalidDataError,
    OperationFailedError,
)
from graceful_error_recovery import perform_critical_operation


class TestErrorHandlingChallenge(unittest.TestCase):
    def test_read_data_from_file_success(self):
        result = read_data_from_file("/home/labex/project/example.txt")
        self.assertEqual(result, "example content")

    def test_read_data_from_file_failure(self):
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("on_existent_file.txt")

    def test_process_data_success(self):
        try:
            process_data("valid data")
        except InvalidDataError:
            self.fail("process_data() raised InvalidDataError unexpectedly.")

    def test_process_data_failure(self):
        with self.assertRaises(InvalidDataError):
            process_data("")

    def test_perform_critical_operation_success(self):
        with patch("time.sleep"):
            try:
                perform_critical_operation("valid data")
            except OperationFailedError:
                self.fail(
                    "perform_critical_operation() raised OperationFailedError unexpectedly."
                )

    def test_perform_critical_operation_failure(self):
        with patch("time.sleep"):
            perform_critical_operation("")


if __name__ == "__main__":
    unittest.main()
