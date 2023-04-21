# Fire Station Alert System

The fire station is responsible for attending emergencies in a city. Emergencies are reported with a priority level and a location. To manage the emergencies, the station wants to develop an alert system that can add, remove, and prioritize emergencies.

## Example Usage

```python
fs = FireStation()
e1 = Emergency(2, "Main St")
e2 = Emergency(1, "Market St")
fs.add_emergency(e1)
fs.add_emergency(e2)
fs.prioritize_emergencies()
fs.remove_emergency(e1)
```

## TODO

- Complete `fire_emergencies.py`

## Requirements

- Implement a class `Emergency` with attributes `priority` (int) and `location` (str).
- Implement a class `FireStation` with a list `emergencies`.
- Implement a method `add_emergency()` in `FireStation` class to add an emergency to the list.
- Implement a method `remove_emergency()` in `FireStation` class to remove an emergency from the list.
- Implement a method `prioritize_emergencies()` in `FireStation` class to sort the list of emergencies by priority.
- Implement the `__del__` method for the `Emergency` class.
