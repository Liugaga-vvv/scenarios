# Modifying a Mutable Data Type

Next, we'll create and modify a mutable data type together.

```python
# Create two variables `x` and `y` that reference the same list.
x = [1, 2, 3]
y = x

# Modify the list using variable `x`.
x.append(4)

# Observe the changes in variable `y`.
print(y)  # Output: [1, 2, 3, 4] (y also reflects the changes because x and y share the same memory address)
```

In this example, we created two variables `x` and `y` that reference the same list.

When we modified the list using variable `x`, the changes were also reflected in variable `y`. This is because `x` and `y` share the same memory address.
