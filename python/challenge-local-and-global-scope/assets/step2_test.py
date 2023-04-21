import io
import sys

sys.path.append("/home/labex/project")

import unittest
from step2 import outer_function


class TestNestedFunction(unittest.TestCase):
    def test_nested_function(self):
        self.assertEqual(outer_function(), None)

    def test_print_variable(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        outer_function()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "15\n")


if __name__ == "__main__":
    unittest.main()
