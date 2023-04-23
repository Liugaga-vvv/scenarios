# Water Tracker

Your task is to write a Python function called `record_water_intake` that takes in two parameters:

- `water_tracker` (a dictionary): represents the current water intake for the day, where the keys are the times of day in the format "HH:MM" (24-hour clock) and the values are the amount of water in milliliters that was consumed at each time.
- `new_intake` (a tuple): represents the new water intake to be recorded, where the first element is the time of day in the format "HH:MM" (24-hour clock) and the second element is the amount of water in milliliters that was consumed at that time.

## Example Usage

```python
water_tracker = {"09:00": 250, "12:30": 500, "15:45": 350}

new_intake = ("18:00", 200)

total_intake = record_water_intake(water_tracker, new_intake)

print(water_tracker)
print(total_intake)
```

Output:

```python
{'09:00': 250, '12:30': 500, '15:45': 350, '18:00': 200}
1300
```

```python
water_tracker = {"09:00": 250, "12:30": 500, "15:45": 350}

new_intake = ("12:30", 100)

total_intake = record_water_intake(water_tracker, new_intake)

print(water_tracker)
print(total_intake)
```

Output:

```python
{'09:00': 250, '12:30': 600, '15:45': 350}
1200
```

## TODO

- Complete `water_tracker.py`

## Requirements

- The function should update the `water_tracker` dictionary with the new water intake.
- The function should calculate the total amount of water consumed so far in the day and return it.
