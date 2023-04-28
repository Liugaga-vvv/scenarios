import sys

sys.path.append("/home/labex/project")

import unittest
from calculate_bmi import calculate_bmi


class TestCalculateBMI(unittest.TestCase):
    def test_calculate_bmi(self):
        weight = 70.5
        height = 1.75
        expected_output = 23.02
        self.assertAlmostEqual(
            calculate_bmi(weight, height), expected_output, delta=0.01
        )

        weight = 80.0
        height = 1.80
        expected_output = 24.69
        self.assertAlmostEqual(
            calculate_bmi(weight, height), expected_output, delta=0.01
        )

        weight = 65.5
        height = 1.65
        expected_output = 24.06
        self.assertAlmostEqual(
            calculate_bmi(weight, height), expected_output, delta=0.01
        )


if __name__ == "__main__":
    unittest.main()
