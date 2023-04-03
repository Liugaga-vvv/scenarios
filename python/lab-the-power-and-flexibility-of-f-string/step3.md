# F-String Formatting

F-strings support various formatting options, such as padding, alignment, and number formatting. You can use the format specifier syntax inside the curly braces `{}` after an expression, separated by a colon `:`.

## Padding and Alignment

You can use the format specifier to align and pad the result of an expression:

```python
name = "Alice"
print(f"{name:<10}")  # Left-align, pad with spaces to a width of 10
print(f"{name:>10}")  # Right-align, pad with spaces to a width of 10
print(f"{name:^10}")  # Center-align, pad with spaces to a width of 10
```

Output:

```
Alice
     Alice
  Alice
```

## Number Formatting

F-strings also allow you to format numbers using the format specifier:

```python
pi = 3.14159265
print(f"Pi is approximately {pi:.3f}.")  # Format pi with 3 decimal places
```

Output:

```
Pi is approximately 3.142.
```
