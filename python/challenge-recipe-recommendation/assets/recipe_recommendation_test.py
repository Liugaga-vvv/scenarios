import sys

sys.path.append("/home/labex/project")

import unittest
from recipe_recommendation import recommend_recipes


class TestRecipeRecommendation(unittest.TestCase):
    def test_no_match(self):
        recipe_list = [
            {
                "name": "Spaghetti Bolognese",
                "ingredients": [
                    "spaghetti",
                    "ground beef",
                    "tomato sauce",
                    "onion",
                    "garlic",
                ],
            },
            {
                "name": "Chicken Alfredo",
                "ingredients": [
                    "fettuccine",
                    "chicken breast",
                    "heavy cream",
                    "butter",
                    "parmesan cheese",
                ],
            },
            {
                "name": "Vegetable Stir Fry",
                "ingredients": [
                    "rice",
                    "broccoli",
                    "carrots",
                    "onion",
                    "garlic",
                    "soy sauce",
                ],
            },
        ]
        self.assertEqual(recommend_recipes(["spaghetti", "carrots"], recipe_list), [])

    def test_partial_match(self):
        recipe_list = [
            {
                "name": "Spaghetti Bolognese",
                "ingredients": [
                    "spaghetti",
                    "ground beef",
                    "tomato sauce",
                    "onion",
                    "garlic",
                ],
            },
            {
                "name": "Chicken Alfredo",
                "ingredients": [
                    "fettuccine",
                    "chicken breast",
                    "heavy cream",
                    "butter",
                    "parmesan cheese",
                ],
            },
            {
                "name": "Vegetable Stir Fry",
                "ingredients": [
                    "rice",
                    "broccoli",
                    "carrots",
                    "onion",
                    "garlic",
                    "soy sauce",
                ],
            },
        ]
        self.assertEqual(
            recommend_recipes(["spaghetti", "tomato sauce", "garlic"], recipe_list),
            ["Spaghetti Bolognese"],
        )

    def test_exact_match(self):
        recipe_list = [
            {
                "name": "Spaghetti Bolognese",
                "ingredients": [
                    "spaghetti",
                    "ground beef",
                    "tomato sauce",
                    "onion",
                    "garlic",
                ],
            },
            {
                "name": "Chicken Alfredo",
                "ingredients": [
                    "fettuccine",
                    "chicken breast",
                    "heavy cream",
                    "butter",
                    "parmesan cheese",
                ],
            },
            {
                "name": "Vegetable Stir Fry",
                "ingredients": [
                    "rice",
                    "broccoli",
                    "carrots",
                    "onion",
                    "garlic",
                    "soy sauce",
                ],
            },
        ]
        self.assertEqual(
            recommend_recipes(["rice", "broccoli", "soy sauce"], recipe_list),
            ["Vegetable Stir Fry"],
        )


if __name__ == "__main__":
    unittest.main()
