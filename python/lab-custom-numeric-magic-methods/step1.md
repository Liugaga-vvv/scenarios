# Unary Operators

Unary operations are operations that involve a single operand, such as negation, absolute value, etc.

Let's start with a simple object. In `number.py`, create a class named `MyNumber` that have an attribute `value`.

```python
class MyNumber:
    def __init__(self, value: float):
        self.value = value
```

## \_\_neg\_\_

The `__neg__` magic method defines how the negation operation should behave. When you use the `-` operator on an instance of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __neg__(self) -> 'MyNumber':
        """Returns the negation of the instance's value."""
        return MyNumber(-self.value)
```

## \_\_abs\_\_

The `__abs__` magic method defines how the absolute value operation should behave. When you use the `abs()` function on an instance of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __abs__(self) -> 'MyNumber':
        """Returns the absolute value of the instance's value."""
        return MyNumber(abs(self.value))
```

## \_\_round\_\_

The `__round__` magic method defines how the rounding operation should behave. When you use the `round()` function on an instance of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __round__(self, ndigits: int = None) -> 'MyNumber':
        """Rounds the instance's value to the nearest whole number or specified number of digits."""
        return MyNumber(round(self.value, ndigits))


```

## \_\_floor\_\_

The `__floor__` magic method defines how the floor operation should behave. When you use the `math.floor()` function on an instance of your class, this method is called.

```python
# math module should be import at the top of number.py
import math

    # ... (previous code in number.py)

    def __floor__(self) -> 'MyNumber':
        """Returns the largest integer less than or equal to the instance's value."""
        return MyNumber(math.floor(self.value))
```

## \_\_ceil\_\_

The `__ceil__` magic method defines how the ceiling operation should behave. When you use the `math.ceil()` function on an instance of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __ceil__(self) -> 'MyNumber':
        """Returns the smallest integer greater than or equal to the instance's value."""
        return MyNumber(math.ceil(self.value))
```

## Example: Using the Unary Operators

Now that we have defined the unary operators for our `MyNumber` class, let's see how they work in `unary_example.py`:

```python
import math
from number import MyNumber

# Create a new MyNumber object
a = MyNumber(5)
# Use the __neg__ method with the print function
print(f'{a.value=}, {-a.value=}')  # Output: a.value=5, -a.value=-5

# Create another new MyNumber object
a = MyNumber(-5)
# Use the __abs__ method with the print function
print(f'{a.value=}, {abs(a).value=}')  # Output: a.value=-5, abs(a).value=5

# Create the third new MyNumber object
a = MyNumber(5.678)
# Use the __round__ method with the print function
print(f'{a.value=}, {round(a, 2).value=}')  # Output: a.value=5.678, round(a, 2).value=5.68

# Use the __floor__ method with the print function
print(f'{a.value=}, {math.floor(a).value=}')  # Output: a.value=5.678, math.floor(a).value=5

# Use the __ceil__ method with the print function
print(f'{a.value=}, {math.ceil(a).value=}')  # Output: a.value=5.678, math.ceil(a).value=6
```

Then typing the following command in the terminal to execute the script.

```bash
python unary_example.py
```
