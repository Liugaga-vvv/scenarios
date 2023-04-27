import sys

sys.path.append("/home/labex/project")

import unittest
from temperature_converter import temperature_converter


class TestTemperatureConverter(unittest.TestCase):
    def test_temperature_converter(self):
        self.assertEqual(temperature_converter(32), 0.0)
        self.assertEqual(temperature_converter(68), 20.0)
        self.assertEqual(temperature_converter(86), 30.0)


if __name__ == "__main__":
    unittest.main()
