import sys

sys.path.append("/home/labex/project")

import unittest
from find_intersection import find_intersection

class TestFindIntersection(unittest.TestCase):
    def test_intersection(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_intersection(list1, list2), [4, 5])
    
    def test_no_intersection(self):
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]
        self.assertEqual(find_intersection(list1, list2), [])
    
    def test_duplicates(self):
        list1 = [1, 1, 2, 3]
        list2 = [1, 2, 2, 4]
        self.assertEqual(find_intersection(list1, list2), [1, 2])
    
    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertEqual(find_intersection(list1, list2), [])
    
    def test_different_sizes(self):
        list1 = [1, 2, 3]
        list2 = [1, 2, 3, 4, 5]
        self.assertEqual(find_intersection(list1, list2), [1, 2, 3])
    
if __name__ == '__main__':
    unittest.main()
    