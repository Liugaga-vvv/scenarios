import sys

sys.path.append("/home/labex/project")

import unittest

from fake_person import fake_person_list

class TestFakePerson(unittest.TestCase):
    def test_person(self):
        num = 5
        persons = fake_person_list(num)
        self.assertEqual(num, len(persons))
        for i in range(num - 1):
            self.assertTrue(persons[i].getAge() <= persons[i + 1].getAge())


if __name__ == "__main__":
    unittest.main()
