# Word Solitaire

Now, for the word list obtained in the previous step, perform word chaining by following the steps below:

1. First, sort the string list;
2. Starting with the first word as the head, find a word that starts with the last letter of the current word and add it to the word chain of the remaining words. If it does not exist, save the current string;
3. Repeat the previous step with the remaining words until all words are used.

Example:

```python
a = ['a', 'toy', 'has', 'excellent', 'apple']
output:
['a', 'apple', 'excellent', 'toy']
['has']
```

## TODO

- Completing `solitaire.py`

## Requirements

- Each word can be used only once.
- If there are no words, return an empty list.
