# Step 2 Solution

```python
# count the top 3 most frequent words in all the files in a directory.
import os

words_counter = {}
for f in os.listdir('/home/labex/project/files'):
    words = open(os.path.join('/home/labex/project/files', f), 'r').read().split()
    for word in words:
        word = word.strip('.,')
        if word not in words_counter:
            words_counter[word] = 0
        words_counter[word] += 1

for words, count in sorted(words_counter.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(words, count)
```
