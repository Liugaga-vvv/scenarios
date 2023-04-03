# Python Data Types

The list may contain the following data types:

- int
- float
- str
- bool
- list
- tuple
- dict
- set

## TODO

Please complete the function below in the given file `count_data_types.py`.

```python
def count_data_types(data: List[Union[int, float, str, bool, list, tuple, dict, set]]) -> Dict[str, int]:
```

## Input

A list of data types, where 1 <= len(data) <= 10^5.

## Output

A dictionary that contains the count of each data type in the list. The keys of the dictionary should be one of the following: 'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'set'.

## Example

Input:

```
count_data_types([1, 2.5, 'hello', True, [1, 2, 3], (1, 2, 3), {'a': 1, 'b': 2}, {1, 2, 3}])
```

Output:

```
{'int': 1, 'float': 1, 'str': 1, 'bool': 1, 'list': 1, 'tuple': 1, 'dict': 1, 'set': 1}
```

## Requirements

- The input list may contain different types of data in any order.
- Your solution should be efficient in terms of time and space complexity.
