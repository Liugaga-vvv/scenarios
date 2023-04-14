## Step 2 Solution

```python
# print the next 10 days, next 100 days, next 1000 days, and next 10000 days
import datetime
now = datetime.datetime.now()
for i in range(4):
    next_day = now + datetime.timedelta(days=10**(i+1))
    print(next_day.strftime('%Y-%m-%d'))
```
