# Step 3 Solution

```python
import os
import shutil

def folder_delete(folder: str) -> int:
    """
    This function delete folder
    :param folder: The name of the folder to be deleted.
    :return: The count of files in folder.
    """
    if os.path.isdir(folder):
        file_len = len(os.listdir(folder))
        shutil.rmtree(folder)
    else:
        file_len = 0
    return file_len
```
