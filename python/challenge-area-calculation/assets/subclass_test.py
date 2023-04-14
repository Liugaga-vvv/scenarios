import sys

sys.path.append("/home/labex/project")
from subclass import Circle, Square

import unittest


class TestSubclass(unittest.TestCase):
    def test_area_method(self):
        length = 3
        circle = Circle(length)
        self.assertTrue(circle.area() - 3.14 * length * length < 0.01)

        square = Square(length)
        self.assertTrue(square.area() - length * length < 0.01)


if __name__ == "__main__":
    unittest.main()
