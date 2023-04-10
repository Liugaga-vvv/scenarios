# Sum and Sorted

There are several baskets, each containing fruits of different weights. Please calculate the total weight of the fruits in each basket and return them in order.

example of input:

```json
{
  "apple": [1, 2.3, 4, 5],
  "orange": [3],
  "banana": [4, 5, 6]
}
```

return value example:

```json
[
  {
    "name": "banana",
    "weight": 15
  },
  {
    "name": "apple",
    "weight": 12.3
  },
  {
    "name": "orange",
    "weight": 3
  }
]
```

## TODO

- Completing `basket_weight.py`

## Requirements

- If the number of baskets is 0, return an empty list.
- The return results must be in descending order of weight.
