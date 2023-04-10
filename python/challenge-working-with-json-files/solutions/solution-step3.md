## Step 3 Solution

```python
# read a JSON file and retrieves the value for a specific key
import os
import sys
import json

filename, key = sys.argv[1:]
filename = os.path.join('json_files', filename)
if os.path.isfile(filename):
    data = json.load(open(filename, 'r'))
    if key in data:
        print(f'The value for the key {key} in {filename} is {data[key]}.')
```
