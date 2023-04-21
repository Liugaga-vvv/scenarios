from typing import List, Dict


def recommend_recipes(
    ingredients: List[str], recipe_list: List[Dict[str, List[str]]]
) -> List[str]:
    recommended_recipes = []

    for recipe in recipe_list:
        recipe_ingredients = recipe["ingredients"]

        if all(ingredient in recipe_ingredients for ingredient in ingredients):
            recommended_recipes.append(recipe["name"])

    return recommended_recipes
