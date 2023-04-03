# String Representation

## Target

Implement a class MyString that takes a string as an argument to the constructor. The class should have a `__repr__` magic method that returns a string representation of the object.

For example:

I get the `s1` object by calling the `MyString` class, pass the `s1` object into the `repr` function, The output of the `print` function should be 'MyString('Hello')'.

```python
s1 = MyString('Hello')

print(repr(s1))
# Output: MyString('Hello')
```

## Requirements

- Implement the class `MyString` in `string_concatenation.py`.
- Implement the `__repr__` magic method to concatenate two strings.
