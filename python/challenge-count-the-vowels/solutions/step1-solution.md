# Solution

```python
def count_vowels(string: str) -> int:
    vowels = set("aeiou")
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
```
