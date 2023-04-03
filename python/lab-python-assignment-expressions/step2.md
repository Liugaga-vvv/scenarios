# Using Assignment Expressions in a Conditional Statement

In this step, we will explore the usage of assignment expressions within a conditional statement.

```python
# Using assignment expressions in a conditional statement
input_str = "Hello, world!"
if (length := len(input_str)) > 10:
    print(f"The string has {length} characters, which is more than 10.")
else:
    print(f"The string has {length} characters, which is less than or equal to 10.")
```

Output:

```python
The string has 13 characters, which is more than 10.
```

Here, we calculate the length of `input_str` and assign it to the variable `length` using the walrus operator within the condition of the `if` statement. This allows us to use the value of `length` in both branches of the conditional.
