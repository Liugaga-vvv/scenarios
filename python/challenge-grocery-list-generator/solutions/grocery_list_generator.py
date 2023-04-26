from typing import List, Tuple


def generate_grocery_list(meal_plan: List[Tuple[str, List[str]]]) -> List[str]:
    unique_ingredients = set()

    for meal in meal_plan:
        unique_ingredients.update(meal[1])

    return list(unique_ingredients)
