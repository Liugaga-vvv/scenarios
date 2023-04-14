# Basic Types

Type hints for basic types are straightforward. Just use the type itself as a hint.

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

1. Define a variable of type `int`, assign it a value, and print it.

```python
age: int = 25
print(age) #Output: 25
```

2. Define a variable of type `float`, assign a value, and print it.

```python
temperature: float = 98.6
print(temperature) # Output: 98.6
```

3. Define a variable of type `bool`, assign it a value, and print it.

```python
is_raining: bool = True
print(is_raining) # Output: True
```

4. Define a variable of type `str`, assign a value, and print it.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice")) # Output: Hello, Alice!
```

5. Define a function that takes two arguments of type `int`, multiplies them, and returns the result as an `int`.

```python
def multiply(x: int, y: int) -> int:
    return x * y

result = multiply(5, 10)
print(result) # Output: 50
```
