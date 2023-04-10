import sys

sys.path.append("/home/labex/project")

import unittest

from person import Person


class TestPerson(unittest.TestCase):
    def test_person(self):
        person = Person('name', age=3, email='abc@a.com')
        self.assertEqual(3, person.getAge())


if __name__ == "__main__":
    unittest.main()
