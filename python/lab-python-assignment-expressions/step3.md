# Using Assignment Expressions in a Loop

Now, let's see how to use assignment expressions in a loop.

```python
# Using assignment expressions in a loop
numbers = [1, 2, 3, 4, 5]
while (n := numbers.pop()) > 2:
    print(f"Popped {n}, which is greater than 2.")
print(f"Popped {n}, which is less than or equal to 2.")
```

Output:

```python
Popped 5, which is greater than 2.
Popped 4, which is greater than 2.
Popped 3, which is greater than 2.
Popped 2, which is less than or equal to 2
```

In this example, we use the walrus operator within the condition of the `while` loop to pop elements from the `numbers` list and assign them to the variable `n`. The loop continues until an element less than or equal to 2 is popped.
