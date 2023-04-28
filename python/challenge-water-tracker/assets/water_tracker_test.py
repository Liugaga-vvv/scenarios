import sys

sys.path.append("/home/labex/project")

import unittest
from water_tracker import record_water_intake


class TestRecordWaterIntake(unittest.TestCase):
    def test_record_water_intake(self):
        water_tracker = {"09:00": 250, "12:30": 500, "15:45": 350}
        new_intake = ("18:00", 200)
        expected_tracker = {"09:00": 250, "12:30": 500, "15:45": 350, "18:00": 200}
        expected_intake = 1300
        self.assertEqual(
            record_water_intake(water_tracker, new_intake), expected_intake
        )
        self.assertEqual(water_tracker, expected_tracker)

        water_tracker = {"09:00": 250, "12:30": 500, "15:45": 350}
        new_intake = ("12:30", 100)
        expected_tracker = {"09:00": 250, "12:30": 600, "15:45": 350}
        expected_intake = 1200
        self.assertEqual(
            record_water_intake(water_tracker, new_intake), expected_intake
        )
        self.assertEqual(water_tracker, expected_tracker)


if __name__ == "__main__":
    unittest.main()
