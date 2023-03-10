import sys


sys.path.append("/home/labex/project")

import unittest
import numpy as np
from generate_graph import generate_graph

class TestGenerateGraph(unittest.TestCase):

    def test_generate_graph(self):
        n = 4
        p = 0.3
        result = generate_graph(n, p)
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, (n, n))
        self.assertTrue(np.all(result == result.T))

if __name__ == '__main__':
    unittest.main()