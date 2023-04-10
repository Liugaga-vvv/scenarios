# Static Type Checking

In Python, static type checking can be done using type hints and a static type checker like [mypy](https://mypy.readthedocs.io/en/stable/index.html). Type hints indicate the expected types of variables, function arguments, and return values. Here's an example:

First, install `mypy`.

```bash
pip install mypy
```

Here's an example:

Create a Project called `mypy.py` in the WebIDE and enter the following content.

```python
def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(2, 3)
print(result)
```

Then run `mypy` on your script.

```bash
mypy mypy.py
```

This will give you feedback on any type inconsistencies found in your code.
