## Step 2 Solution

create a python script and execute the code:

```python
# merges all list values across JSON files in a directory and writes the merged list to a new JSON file
import os
import json

merged = []
for filename in os.listdir('/home/labex/project/json_files'):
    data = json.load(open(os.path.join('/home/labex/project/json_files', filename), 'r'))
    for value in data.values():
        if isinstance(value, list):
            merged.append(value)
with open('/home/labex/project/list.json', 'w') as f:
    json.dump(merged, f)
```
