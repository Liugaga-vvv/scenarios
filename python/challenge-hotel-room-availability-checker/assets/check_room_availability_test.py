import sys

sys.path.append("/home/labex/project")

import unittest
from check_room_availability import check_room_availability
from unittest.mock import patch
import io


class TestCheckRoomAvailability(unittest.TestCase):
    def test_check_room_availability(self):
        room_types = ["single", "double", "suite"]
        rooms_available = [0, 1, 5]
        expected_output = "No single rooms available\n1 double room available\n5 suite rooms available\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            check_room_availability(room_types, rooms_available)
            self.assertEqual(fake_stdout.getvalue(), expected_output)

        room_types = ["twin", "queen", "king"]
        rooms_available = [3, 2, 0]
        expected_output = (
            "3 twin rooms available\n2 queen rooms available\nNo king rooms available\n"
        )
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            check_room_availability(room_types, rooms_available)
            self.assertEqual(fake_stdout.getvalue(), expected_output)

        room_types = ["economy", "standard", "deluxe"]
        rooms_available = [1, 0, 10]
        expected_output = "1 economy room available\nNo standard rooms available\n10 deluxe rooms available\n"
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            check_room_availability(room_types, rooms_available)
            self.assertEqual(fake_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
