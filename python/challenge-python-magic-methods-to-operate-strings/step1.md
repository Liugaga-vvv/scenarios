# String Concatenation

## Target

Implement a class MyString that takes a string as an argument to the constructor. The class should have a `__add__` magic method that concatenates two `MyString` objects.

For example:

Given `s1 = MyString('Hello')` and `s2 = MyString('World')`, and then add up s1 and s2. The output of the `print` function should be 'HelloWorld'.

```python
s1 = MyString('Hello')

s2 = MyString('World')

print(s1+s2)
# Output: HelloWorld
```

## Requirements

- Implement the class `MyString` in `string_concatenation.py`.
- Implement the `__add__` magic method to concatenate two strings.
