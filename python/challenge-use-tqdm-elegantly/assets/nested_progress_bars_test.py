import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch
from io import StringIO
from time import sleep
from nested_progress_bars import nested_progress_bars


class TestProgressBarSolutions(unittest.TestCase):
    def test_nested_progress_bars(self):
        tasks = [[0.1, 0.2], [0.2, 0.1, 0.3], [0.1, 0.1]]

        with patch('sys.stderr', new=StringIO()) as captured_output:
            nested_progress_bars(tasks)
            output = captured_output.getvalue()

        self.assertIn("Main Task", output)
        self.assertIn("Sub-Task", output)
        self.assertIn("100%", output)

if __name__ == '__main__':
    unittest.main()
