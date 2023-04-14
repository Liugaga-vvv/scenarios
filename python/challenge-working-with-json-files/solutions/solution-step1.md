## Step 1 Solution

```python
# counts the total number of elements across all JSON files in a directory
import os
import json

count = 0
for filename in os.listdir('/home/labex/project/json_files'):
    data = json.load(open(os.path.join('/home/labex/project/json_files', filename), 'r'))
    count += len(data)
print(count)
```
