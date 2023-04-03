# In-place Operations

In-place operations are operations that modify the value of an object in place, without creating a new object. They are denoted by the augmented assignment operators such as `+=`, `-=`, `*=`, `/=`, etc.

If the in-place operator is not defined for a Python class, then the binary operator will be used instead when an in-place operation is attempted.

There is an example in `inplace_example1.py`, change the binary operators to in-place operators:

```python
from number import MyNumber

# Create two new MyNumber objects
a = MyNumber(5)
b = MyNumber(3)
print(f'{a.value=}, {b.value=}') # Output: a.value=5, b.value=3

a += b
# Use the __add__ method with the print function
print(f'after a+=b: {a.value=}')  # Output:after a+=b: (a+b).value=8
```

To run the example, type the following command in the terminal:

```bash
python inplace_example1.py
```

The result shows that the `__add__` was used when attempted the `+=` operation.

Then we will implement in-place operations in `MyNumber`, and their behaviour with the corresponding binary operators will be slightly different.

## \_\_iadd\_\_

The `__iadd__` magic method defines how the in-place addition operation should behave. When you use the `+=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __iadd__(self, other: 'MyNumber') -> 'MyNumber':
        """Adds the other instance's value to the instance's value in-place."""
        print(f'input: {self.value=}, {other.value=}')
        self.value += other.value
        print(f'after +=: {self.value=}')
        return self
```

## \_\_isub\_\_

The `__isub__` magic method defines how the in-place subtraction operation should behave. When you use the `-=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __isub__(self, other: 'MyNumber') -> 'MyNumber':
        """Subtracts the other instance's value from the instance's value in-place."""
        print(f'input: {self.value=}, {other.value=}')
        self.value -= other.value
        print(f'after -=: {self.value=}')
        return self
```

## \_\_imul\_\_

The `__imul__` magic method defines how the in-place multiplication operation should behave. When you use the `*=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __imul__(self, other: 'MyNumber') -> 'MyNumber':
        """Multiplies the instance's value by the other instance's value in-place."""
        print(f'input: {self.value=}, {other.value=}')
        self.value *= other.value
        print(f'after *=: {self.value=}')
        return self
```

## \_\_itruediv\_\_

The `__itruediv__` magic method defines how the in-place true division operation should behave. When you use the `/=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __itruediv__(self, other: 'MyNumber') -> 'MyNumber':
        """Divides the instance's value by the other instance's value in-place."""
        print(f'input: {self.value=}, {other.value=}')
        self.value /= other.value
        print(f'after /=: {self.value=}')
        return self
```

## \_\_ifloordiv\_\_

The `__ifloordiv__` magic method defines how the in-place floor division operation should behave. When you use the `//=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __ifloordiv__(self, other: 'MyNumber') -> 'MyNumber':
        """Performs in-place floor division on the instance's value by the other instance's value."""
        print(f'input: {self.value=}, {other.value=}')
        self.value //= other.value
        print(f'after //=: {self.value=}')
        return self
```

## \_\_imod\_\_

The `__imod__` magic method defines how the in-place modulo operation should behave. When you use the `%=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __imod__(self, other: 'MyNumber') -> 'MyNumber':
        """Performs in-place modulo operation on the instance's value by the other instance's value."""
        print(f'input: {self.value=}, {other.value=}')
        self.value %= other.value
        print(f'after %=: {self.value=}')
        return self
```

## \_\_ipow\_\_

The `__ipow__` magic method defines how the in-place power operation should behave. When you use the `**=` operator on instances of your class, this method is called.

```python
    # ... (previous code in number.py)

    def __ipow__(self, other: 'MyNumber') -> 'MyNumber':
        """Raises the instance's value to the power of the other instance's value in-place."""
        print(f'input: {self.value=}, {other.value=}')
        self.value **= other.value
        print(f'after **=: {self.value=}')
        return self
```

## Example: Using the In-place Operations

Now that we have defined the in-place operators for our `MyNumber` class, let's see how they work in `example3.py`:

```python
from number import MyNumber

# Create a new MyNumber objects
a = MyNumber(13)

# Use the __iadd__ method
a += MyNumber(5)
# Output:
# input: self.value=13, other.value=5
# after +=: self.value=18

# Use the __isub__ method
a -= MyNumber(5)
# Output:
# input: self.value=18, other.value=5
# after -=: self.value=13

# Use the __imul__ method
a *= MyNumber(5)
# Output:
# input: self.value=13, other.value=5
# after *=: self.value=65

# Use the __itruediv__ method
a /= MyNumber(5)
# Output:
# input: self.value=65, other.value=5
# after /=: self.value=13.0

# Use the __ifloordiv__ method
a //= MyNumber(2)
# Output:
# input: self.value=13.0, other.value=2
# after //=: self.value=6.0

# Use the __imod__ method
a %= MyNumber(4)
# Output:
# input: self.value=6.0, other.value=4
# after %=: self.value=2.0

# Use the __ipow__ method
a **= MyNumber(3)
# Output:
# input: self.value=2.0, other.value=3
# after **=: self.value=8.0
```

Then typing the following command in the terminal to execute the script.

```bash
python inplace_example2.py
```
