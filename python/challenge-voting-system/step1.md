# Voting System

Write a Python function that takes a list of votes as input and returns the name of the candidate who received the most votes. If there is a tie, the function should return "Tie". The list of votes will contain the name of the candidate that the user voted for.

## Example Usage

```python
votes = ["john", "John", "Mary", "mary", "Peter", "PETER", "john"]

winner = calculate_winner(votes)
print(winner)  # Output: John
```

## TODO

- Complete `calculate_winner.py`

## Requirements

- The function should be named `calculate_winner` and take a list of votes as input.
- The function should return the name of the candidate who received the most votes.
- If there is a tie, the function should return "Tie".
- The function should be case-insensitive (i.e., "john" and "John" should be considered the same).
- The function should handle ties by returning "Tie".
