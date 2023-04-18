# Long Word Counter

## Problem Description

Write a function called `count_long_words` that takes two arguments: a string and an integer. The function should return the number of words in the string that are longer than the given integer. You can assume that the string only contains alphabetic characters and spaces.

## Requirements

- The input string should not be modified
- The function should return an integer
- The function should ignore punctuation and other non-alphabetic characters
- The function should be case-insensitive

## Example Usage

```python
text = "The quick brown fox jumps over the lazy dog"
count = count_long_words(text, 4)
print(count) # 3
```
