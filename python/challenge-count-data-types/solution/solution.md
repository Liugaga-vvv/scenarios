# Solution

```python
from typing import List, Union, Dict

def count_data_types(data: List[Union[int, float, str, bool, list, tuple, dict, set]]) -> Dict[str, int]:
    """
    Count the number of each data type in the list of data.

    Args:
    data: A list of data types.

    Returns:
    A dictionary that contains the count of each data type in the list. The keys of the dictionary should be one of the following: 'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'set'.

    """
    count = {'int': 0, 'float': 0, 'str': 0, 'bool': 0, 'list': 0, 'tuple': 0, 'dict': 0, 'set': 0}
    for item in data:
        if type(item) == int:
            count['int'] += 1
        elif type(item) == float:
            count['float'] += 1
        elif type(item) == str:
            count['str'] += 1
        elif type(item) == bool:
            count['bool'] += 1
        elif type(item) == list:
            count['list'] += 1
        elif type(item) == tuple:
            count['tuple'] += 1
        elif type(item) == dict:
            count['dict'] += 1
        elif type(item) == set:
            count['set'] += 1
    return count
```
