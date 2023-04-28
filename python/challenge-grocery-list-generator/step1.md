# Grocery List Generator

## Problem Description:

You will be given a list of tuples, where each tuple represents a meal. Each tuple contains the following information:

- the name of the meal (a string)
- a list of ingredients (a list of strings)

Your program should process this data and provide the following information:

- a list of all the unique ingredients needed for the week

## TODO

- Complete `grocery_list_generator.py`

## Requirements:

- Define a function `generate_grocery_list(meal_plan: List[Tuple[str, List[str]]]) -> List[str]` that takes in a list of meal plans and returns a list of all the unique ingredients needed for the week.
- The function should be able to handle an empty meal plan and return an empty list.
- The function should use a set to get the unique ingredients.

## Example Usage:

```
meal_plan = [('Spaghetti Bolognese', ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic', 'parmesan cheese']),
             ('Chicken Stir Fry', ['chicken breast', 'broccoli', 'carrots', 'soy sauce', 'rice']),
             ('Caesar Salad', ['romaine lettuce', 'croutons', 'parmesan cheese', 'caesar dressing'])]
generate_grocery_list(meal_plan)
```

Output:

```
['garlic', 'onion', 'parmesan cheese', 'carrots', 'broccoli', 'tomato sauce', 'romaine lettuce', 'rice', 'soy sauce', 'spaghetti', 'croutons', 'chicken breast']
```
