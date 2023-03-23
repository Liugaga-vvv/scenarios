# Simple Assignment Expression

In this step, we will start with a simple example to understand the basic syntax of assignment expressions.

## Open the Python Shell

Open the Python shell by typing the following command in the terminal.

```bash
python3
```

## Simple Test

Let's start with a simple example

```python
# Basic example of an assignment expression
n = 5
result = (squared := n * n)
print(squared, result)
```

Output:

```python
25 25
```

Here, we assign the result of `n * n` to the variable `squared` using the walrus operator `:=` within the parentheses. Then, we assign the value of `squared` to the variable `result`. Finally, we print the values of `squared` and `result`.
