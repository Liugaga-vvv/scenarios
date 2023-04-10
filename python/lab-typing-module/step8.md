# Newtype

NewType is a type hint from the typing module in Python that allows you to create a new type that is just a wrapper around an existing type. This can be useful for adding more semantic meaning to variables and function arguments.

Here's an example:

Create a Project called `newtype.py` in the WebIDE and enter the following content.

Then execute the following python script.

```python
from typing import NewType

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)

def get_order(order_id: OrderId) -> str:
    return f"Order with ID: {order_id}"

order_id = OrderId(123)
user_id = UserId(123)

print(get_order(order_id))  # Output: Order with ID: 123
```

Use the following command to run the script.

```bash
python newtype.py
```
