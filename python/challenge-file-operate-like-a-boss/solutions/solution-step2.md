# Step 2 Solution

```python
import os
import shutil

def file_move(file: str, folder: str) -> None:
    """
    This function move file to a new location
    :param file: The name of the file to be moved.
    :param folder: The name of the folder to move the file to.
    :return: None
    """

    if os.path.isfile(file):
        if not os.path.isdir(folder):
            os.mkdir(folder)
        shutil.move(file, folder)
```
