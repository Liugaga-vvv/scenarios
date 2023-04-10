# Callable

The `Callable` type is used to specify the type of a function or method.

Create a Project called `callable.py` in the WebIDE and enter the following content.

```python
from typing import Callable

def apply_function(value: int, func: Callable[[int], int]) -> int:
    return func(value)

def double(x: int) -> int:
    return x * 2

print(apply_function(5, double))  # Output: 10
```

Use the following command to run the script.

```bash
python callable.py
```
