import io
import sys

sys.path.append("/home/labex/project")

import unittest
from step1 import update_global_variable, update_local_variable, global_var, local_var


class TestVariables(unittest.TestCase):
    def test_update_global_variable(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        update_global_variable()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            captured_output.getvalue(), "Global variable inside function: 10\n"
        )

    def test_update_local_variable(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        update_local_variable()
        sys.stdout = sys.__stdout__
        self.assertEqual(
            captured_output.getvalue(), "Local variable inside function: 5\n"
        )

    def test_global_variable_outside_function(self):
        self.assertEqual(global_var, 10)

    def test_local_variable_outside_function(self):
        self.assertEqual(local_var, 0)


if __name__ == "__main__":
    unittest.main()
