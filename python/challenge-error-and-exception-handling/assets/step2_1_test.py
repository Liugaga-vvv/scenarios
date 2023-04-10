import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch

from graceful_error_recovery import perform_critical_operation


class TestStep2(unittest.TestCase):
    def test_perform_critical_operation_has_data(self):
        with patch("time.sleep"):
            perform_critical_operation("example content")


if __name__ == "__main__":
    unittest.main()
