# Variable Assignment and Memory Addresses

In Python, variables are just references to memory locations where values are stored. When you assign a value to a variable, Python creates a new object (if necessary) and makes the variable refer to that object.

Open the Python interpreter first:

```python
python
```

Let's see an example:

```python
x = 10
y = x
```

In this example, the variable `x` is assigned the value `10`. When we assign `x` to `y`, both variables now reference the same memory location. We can check this using the `id()` function:

```python
print(id(x))  # Output: memory address of x
print(id(y))  # Output: memory address of y, which should be the same as x
```

## The `is` Operator

In Python, the `is` operator compares the memory addresses of two objects. If the memory addresses are the same, the `is` operator returns `True`; otherwise, it returns `False`. This is different from the `==` operator, which compares the values of the objects.

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # Output: True (x and y have the same memory address)
print(x is z)  # Output: False (x and z have different memory addresses)
```
