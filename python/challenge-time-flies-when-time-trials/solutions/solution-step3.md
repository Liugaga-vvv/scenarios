## Step 3 Solution

```python
from datetime import datetime

def date_time_convert(date_str: str, time_str: str) -> None:
    """Convert date time to Python date format "%B %d, %Y %I:%M %p" and print.
    Args:
        date_str (str): date string.
        time_str (srt): time string.
    """
    # Parse the date and time strings into separate variables
    date_parts = date_str.split("-")
    time_parts = time_str.split(":")

    # Convert the date and time parts to integers
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    second = int(time_parts[2])

    # Create a datetime object using the parsed date and time parts
    dt = datetime(year, month, day, hour, minute, second)
    formatted_dt = dt.strftime("%B %d, %Y %I:%M %p")
    print(formatted_dt)
```
