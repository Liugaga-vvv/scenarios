# Find Expressions

You are given a list of integers `nums` and a target integer `target`. Your task is to find all possible mathematical expressions that can be formed by combining the integers in `nums` using the mathematical operators `+`, `-`, `*`, and `/`. The expressions should evaluate to target.

## Input

- `nums` - A list of `n (2 <= n <= 20)` integers where each integer is within the range `[-10^9, 10^9]`.
- `target` - An integer is within the range `[-10^9, 10^9]`.

## Output

- A list of all possible mathematical expressions that can be formed by combining the integers in nums using the mathematical operators `+`, `-`, `*`, and `/`. The expressions should evaluate to target.
- If there are no valid expressions, the function should return an empty list `[]`.

## Example

```python
# Input:
nums = [1, 2, 3, 4]
target = 5
# Output:
['1+4', '2+3']
```

```python
# Input:
nums = [2, 3, 4, 5]
target = 8
# Output:
['2*4', '3+5']
```

```python
# Input:
nums = [2, 3, 4, 14]
target = 7
# Output:
['14/2', '3+4']
```

## Note

- All the integers in `nums` are unique.
- The order of the integers in the expressions does not matter (`2+4`==`4+2`, Don't appear twice).
- The order of expressions follows the lowest order of integers in nums for each expression.
