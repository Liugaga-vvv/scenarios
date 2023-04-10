import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch

from automated_testing import TestErrorHandlingChallenge


class TestStep3(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testErrorHandlingChallenge = TestErrorHandlingChallenge()

    def test_positive_examples(self):
        with patch(
            "builtins.open",
            new_callable=unittest.mock.mock_open,
            read_data="example content",
        ):
            self.testErrorHandlingChallenge.test_read_data_from_file_success()

        with self.assertRaises(AssertionError):
            with patch(
                "builtins.open",
                new_callable=unittest.mock.mock_open,
                read_data="valid data",
            ):
                self.testErrorHandlingChallenge.test_read_data_from_file_success()

        self.testErrorHandlingChallenge.test_process_data_success()
        self.testErrorHandlingChallenge.test_perform_critical_operation_success()

    def test_reverse_example(self):
        self.testErrorHandlingChallenge.test_read_data_from_file_failure()
        self.testErrorHandlingChallenge.test_process_data_failure()
        self.testErrorHandlingChallenge.test_perform_critical_operation_failure()


if __name__ == "__main__":
    unittest.main()
