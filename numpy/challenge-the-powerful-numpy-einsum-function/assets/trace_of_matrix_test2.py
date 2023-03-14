import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from trace_of_matrix import trace

class TestTrace(unittest.TestCase):
    def test_trace(self):
        A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected_result = 15
        self.assertEqual(trace(A), expected_result)

if __name__ == '__main__':
    unittest.main()