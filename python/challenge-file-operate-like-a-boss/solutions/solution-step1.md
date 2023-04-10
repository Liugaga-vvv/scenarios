# Step 1 Solution

```python
import os

def folder_create(folder: str) -> None:
    """
    This function create folder
    :param folder: The name of the folder to be created.
    :return: None
    """

    if os.path.isdir(folder):
        return
    os.mkdir(folder)
```
