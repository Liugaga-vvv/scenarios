import sys

sys.path.append("/home/labex/project")
import unittest
from typing import List, Tuple
from grocery_list_generator import generate_grocery_list


class TestGenerateGroceryList(unittest.TestCase):
    def test_generate_grocery_list(self):
        meal_plan = [
            (
                "Spaghetti and Meatballs",
                ["spaghetti", "ground beef", "tomato sauce", "onion", "garlic"],
            ),
            ("Caesar Salad", ["romaine lettuce", "Caesar dressing", "croutons"]),
            (
                "Teriyaki Chicken",
                ["chicken thighs", "teriyaki sauce", "rice", "broccoli", "carrots"],
            ),
        ]

        expected_grocery_list = [
            "rice",
            "ground beef",
            "garlic",
            "tomato sauce",
            "onion",
            "broccoli",
            "chicken thighs",
            "romaine lettuce",
            "teriyaki sauce",
            "Caesar dressing",
            "croutons",
            "carrots",
            "spaghetti",
        ]

        self.assertCountEqual(generate_grocery_list(meal_plan), expected_grocery_list)


if __name__ == "__main__":
    unittest.main()
