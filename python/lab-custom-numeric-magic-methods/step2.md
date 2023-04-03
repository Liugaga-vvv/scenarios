# Binary Operators

Binary operations are operations that involve two operands, such as arithmetic operations like addition, subtraction, multiplication, and division, as well as comparison operations like equality, inequality, less than, greater than, etc.

## \_\_add\_\_

The `__add__` magic method defines how the addition operation should behave. When you use the `+` operator on

instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __add__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the sum of the instance's value and the other instance's value."""
        return MyNumber(self.value + other.value)
```

## \_\_sub\_\_

The `__sub__` magic method defines how the subtraction operation should behave. When you use the `-` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __sub__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the difference of the instance's value and the other instance's value."""
        return MyNumber(self.value - other.value)
```

## \_\_mul\_\_

The `__mul__` magic method defines how the multiplication operation should behave. When you use the `*` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __mul__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the product of the instance's value and the other instance's value."""
        return MyNumber(self.value * other.value)
```

## \_\_truediv\_\_

The `__truediv__` magic method defines how the true division operation should behave. When you use the `/` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __truediv__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the result of dividing the instance's value by the other instance's value."""
        return MyNumber(self.value / other.value)
```

## \_\_floordiv\_\_

The `__floordiv__` magic method defines how the floor division operation should behave. When you use the `//` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __floordiv__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the largest integer less than or equal to the result of dividing the instance's value by the other instance's value."""
        return MyNumber(self.value // other.value)
```

## \_\_mod\_\_

The `__mod__` magic method defines how the modulo operation should behave. When you use the `%` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __mod__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the remainder of dividing the instance's value by the other instance's value."""
        return MyNumber(self.value % other.value)
```

## \_\_pow\_\_

The `__pow__` magic method defines how the power operation should behave. When you use the `**` operator or the `pow()` function on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __pow__(self, other: 'MyNumber') -> 'MyNumber':
        """Returns the instance's value raised to the power of the other instance's value."""
        return MyNumber(self.value ** other.value)
```

## Example: Using the Binary Operators

Now that we have defined the binary operators for our `MyNumber` class, let's see how they work in `binary_example.py`:

```python
from number import MyNumber

# Create two new MyNumber objects
a = MyNumber(5)
b = MyNumber(3)
print(f'{a.value=}, {b.value=}') # Output: a.value=5, b.value=3

# Use the __add__ method with the print function
print(f'{(a+b).value=}')  # Output: (a+b).value=8

# Use the __sub__ method with the print function
print(f'{(a-b).value=}')  # Output: (a-b).value=2

# Use the __mul__ method with the print function
print(f'{(a*b).value=}')  # Output: (a*b).value=15

# Use the __truediv__ method with the print function
print(f'{(a/b).value=}')  # Output: (a/b).value=1.6666666666666667

# Use the __floordiv__ method with the print function
print(f'{(a//b).value=}')  # Output: (a//b).value=1

# Use the __mod__ method with the print function
print(f'{(a%b).value=}')  # Output: (a%b).value=2

# Use the __pow__ method with the print function
print(f'{(a**b).value=}')  # Output: (a**b).value=125
```

Then typing the following command in the terminal to execute the script.

```bash
python binary_example.py
```
