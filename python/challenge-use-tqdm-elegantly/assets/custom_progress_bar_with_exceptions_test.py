import sys

sys.path.append("/home/labex/project")

import unittest
from unittest.mock import patch
from io import StringIO
from time import sleep
from custom_progress_bar_with_exceptions import custom_progress_bar_with_exceptions

class TestProgressBarSolutions(unittest.TestCase):
    def test_custom_progress_bar_with_exceptions(self):
        tasks = [0.1, 0.2, 0.3, 0.2, 0.1]

        with patch('sys.stderr', new=StringIO()) as captured_output:
            with patch('custom_progress_bar_with_exceptions.sleep', side_effect=[None, None, KeyboardInterrupt, None, None]):
                custom_progress_bar_with_exceptions(
                    tasks, desc="process 3")
                output = captured_output.getvalue()

        self.assertIn("process 3", output)
        self.assertNotIn("100%", output)

if __name__ == '__main__':
    unittest.main()