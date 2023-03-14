# Implementing List Slicing

In this sub-challenge, you will implement slicing operations in the `MagicList` class.

## Requirements

- The class should support slicing with the colon notation (`:`).
- The class should support negative indices in slicing.

### Getitem Method

In the `__getitem__` method, there are two branches:

- If index is an int type, you can get the item by indexing the list.
- If index is a slice type, you can get the item by slicing the list.

The syntax of slicing is:

```python
list[start:stop:step]
```

- `start` is the starting position of slicing.
- `stop` is the end position of slicing.
- `step` is the step length of slicing.

### Setitem Method

In `__setitem__` method, there are two branches:

- If index is an int type, you can set value at the given index.
- If index is a slice type, you can set value at the given slice.

## TODO

- Continue to complete `magic_list.py`.
- Add the necessary magic methods to support slicing in the `MagicList` class.
