# Function Parameters

In this step, we will explore how the `is` operator can be used with function parameters.

1. Define a function `my_function()` that takes two parameters, `x` and `y`.

```python
def my_function(x, y):
    print(x is y)
```

2. Call the function `my_function()` twice, once with immutable objects and once with mutable objects.

```python
my_function(10, 10)
my_function([], [])
```

The output of the first call should be `True` and the output of the second call should be `False`.
