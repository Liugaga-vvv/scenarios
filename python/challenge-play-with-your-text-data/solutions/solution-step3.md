# Step 3 Solution

create output folder:

```bash
mkdir output
```

then, create a python script and execute:

```python
# read multiple files and writes the n-th word of each file to n-th file
import os

words_list = []

max_len = 0

for f in os.listdir('/home/labex/project/files'):
    texts = open(os.path.join('/home/labex/project/files', f), 'r').read().split()
    texts = [text.strip(',.') for text in texts]
    words_list.append(texts)
    max_len = max_len if max_len > len(texts) else len(texts)

for i in range(max_len):
    words = []
    for word_list in words_list:
        if i < len(word_list):
            words.append(word_list[i])
    open(f'/home/labex/project/output/{i+1}', 'w').write(' '.join(words))
```
