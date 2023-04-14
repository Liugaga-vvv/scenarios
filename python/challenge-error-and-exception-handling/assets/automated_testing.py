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

        # TODO: Verify that the output is the contents of example.txt.

        result = read_data_from_file("/home/labex/project/example.txt")

    def test_read_data_from_file_failure(self):

        # TODO: Verify that a FileNotFoundError exception is caught when an incorrect file name is passed in.

        read_data_from_file("non_existent_file.txt")

    def test_process_data_success(self):

        # TODO: Verify that a InvalidDataError exceptions are raised when normal data is passed in.

        process_data("valid data")

    def test_process_data_failure(self):

        # TODO: Verify that a InvalidDataError exception is caught when an empty string is passed in.

        process_data("")

    def test_perform_critical_operation_success(self):

        # TODO: Verify that a OperationFailedError exceptions are raised when normal data is passed in.

        perform_critical_operation("valid data")

    def test_perform_critical_operation_failure(self):

        # TODO: Verify that a OperationFailedError exception is caught when an empty string is passed in.

        perform_critical_operation("")


if __name__ == "__main__":
    unittest.main()
