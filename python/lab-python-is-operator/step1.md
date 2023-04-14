# Basic Usage

In this step, we will start with the most basic usage of the `is` operator.

1. Open the Python Interpreter in the terminal.

```bash
python3
```

2. Define two variables, `a` and `b`, and assign the same value to both.

```python
a = "Hello"
b = "Hello"
```

3. Print out the memory address of `a` and `b` using the `id()` function.

```python
print(id(a))
print(id(b))
```

4. Use the `is` operator to check if `a` and `b` refer to the same object.

```python
print(a is b)
```

The output of the above code should be `True`, since `a` and `b` refer to the same object in memory.
