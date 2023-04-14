# Dictionary Key-Value Swapper

## Problem Description

Write a Python function named `swap_dict_key_value` that takes a dictionary as an argument, and returns a new dictionary where the keys and values are swapped.

## Requirements

1. The input dictionary may contain any combination of key-value pairs.
2. If a value appears more than once in the input dictionary, only one instance should appear as the key in the output dictionary.
3. All values in the input dictionary are unique.
4. The output dictionary should be sorted alphabetically by keys.

## Example Usage

```python
# Test case 1: empty dictionary
assert swap_dict_key_value({}) == {}

# Test case 2: dictionary with one key-value pair
assert swap_dict_key_value({'a': 1}) == {1: 'a'}

# Test case 3: dictionary with multiple key-value pairs
assert swap_dict_key_value({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}

# Test case 4: dictionary with duplicate values
assert swap_dict_key_value({'a': 1, 'b': 2, 'c': 1}) == {1: 'c', 2: 'b'}

# Test case 5: dictionary with non-integer values
assert swap_dict_key_value({'a': 'one', 'b': 'two', 'c': 'three'}) == {'one': 'a', 'three': 'c', 'two': 'b'}
```
