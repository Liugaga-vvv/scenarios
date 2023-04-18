import sys

sys.path.append("/home/labex/project")

import unittest
from io import StringIO
from print_triangle import print_triangle


class TestPrintTriangle(unittest.TestCase):
    def test_print_triangle(self):
        expected_output = "*\n**\n***\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print_triangle(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

        expected_output = "*\n**\n***\n****\n*****\n"
        captured_output = StringIO()
        sys.stdout = captured_output
        print_triangle(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
