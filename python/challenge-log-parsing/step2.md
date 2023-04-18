# Analysis Each Row

Each line of the log file is split by space like `uri used_time`, in this step we need statistics of each uri requested times, then return the result in directory like:

```
{
    "/create/order": 199,
    "/query/order/info": 20,
    ...
}
```

## Tips

- Use the `directory` to store any uri requested times temporarily.

## TODO

- Completing `uri_count.py`

## Requirements

- Finish the `uri_count` function and return the result.
