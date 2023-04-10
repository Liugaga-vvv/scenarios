# Compare Memory Addresses

In this step, we will compare the memory addresses of variables with the same value.

Please flow the instructions below:

```python
# Create two integer variables `a` and `b` with the same value.
a = 10
b = 10
# Create two list variables `c` and `d` with the same elements.
c = [1, 2, 3]
d = [1, 2, 3]

# Compare the memory addresses of `a` and `b`, as well as `c` and `d`.
print(a is b)  # Output: True
print(c is d)  # Output: False
```

In the example above, we created two integer variables `a` and `b` with the same value.

We also created two list variables `c` and `d` with the same elements.

When we compared the memory addresses of `a` and `b`, the `is` operator returned `True`. This is because `a` and `b` share the same memory address.

However, when we compared the memory addresses of `c` and `d`, the `is` operator returned `False`. This is because `c` and `d` have different memory addresses.

So, what does this mean?

1. Immutable data types with the same value may have the same memory address.
2. Mutable data types with the same value have different memory addresses.
