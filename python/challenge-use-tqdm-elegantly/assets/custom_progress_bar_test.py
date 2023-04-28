import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch
from io import StringIO
from time import sleep
from custom_progress_bar import custom_progress_bar

class TestProgressBarSolutions(unittest.TestCase):

    def test_custom_progress_bar(self):
        tasks = [0.1, 0.2, 0.3, 0.2, 0.1]

        with patch('sys.stderr', new=StringIO()) as captured_output:
            custom_progress_bar(tasks, desc="process 1")
            output = captured_output.getvalue()

        self.assertIn("process 1", output)
        self.assertIn("100%", output)
        
if __name__ == '__main__':
    unittest.main()
