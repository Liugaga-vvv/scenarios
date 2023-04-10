# Step 1 Solution

```python
# count the total number of words in all the files in a directory.
import os

total_len = 0
for f in os.listdir('/home/labex/project/files'):
    total_len += len(open(os.path.join('/home/labex/project/files', f), 'r').read().split())

print(total_len)
```
