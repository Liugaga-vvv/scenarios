# Modifying an Immutable Data Type

Finally, let's work together to modify one immutable data type after another.

```python
# Create two variables `a` and `b` that reference the same string.
a = "hello"
b = a

# Modify the string using variable `a`.
a = a + ", world"

# Observe the changes in variable `b`.
print(b)  # Output: "hello" (b doesn't change because a new object was created when modifying the string)
```

In this example, we created two variables `a` and `b` that reference the same string.

When we modified the string using variable `a`, the changes were not reflected in variable `b`. This is because `a` and `b` have different memory addresses.
