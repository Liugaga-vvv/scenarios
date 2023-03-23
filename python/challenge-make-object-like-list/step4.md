# Implementing List Arithmetic

In this sub-challenge, you will implement arithmetic operations in the `MagicList` class.

## Requirements

- The class should have a `__sub__` method that removes all occurrences of items from the second list in the first list.
- The class should have a `__mul__` method that repeats the list a certain number of times.

### Sub Method

The `__sub__` method uses list comprehension to remove all occurrences of items from the second list in the first list.

The syntax of a list comprehension is:

```python
new_list = [out_expression for item in first_list if condition]
```

- `condition` is a boolean expression, in this step, we judge whether the `item` in the `first_list` doesn't occurr from the second list.

### Mul Method

The `__mul__` method uses `*` operator to repeat the list.

## TODO

- Continue to complete `magic_list.py`.
- Add the necessary magic methods to support arithmetic operations in the `MagicList` class.
