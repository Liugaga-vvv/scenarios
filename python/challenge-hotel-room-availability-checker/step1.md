# Hotel Room Availability Checker

Your task is to write a Python function called `check_room_availability` that takes in two parameters:

- `room_types` (a list of strings): represents the different types of rooms available in the hotel.
- `rooms_available` (a list of integers): represents the number of rooms available for each room type.

The function should check the availability of rooms based on the following criteria:

- If the number of available rooms is 0, print "No {room_type} rooms available".
- If the number of available rooms is 1, print "1 {room_type} room available".
- If the number of available rooms is greater than 1, print "{num_rooms} {room_type} rooms available".

where `{room_type}` represents the room type and `{num_rooms}` represents the number of rooms available.

## Example Usage

```python
room_types = ['single', 'double', 'suite']
rooms_available = [0, 1, 5]

check_room_availability(room_types, rooms_available)
```

Output:

```python
No single rooms available
1 double room available
5 suite rooms available
```

```python
room_types = ['twin', 'queen', 'king']
rooms_available = [3, 2, 0]

check_room_availability(room_types, rooms_available)
```

Output:

```python
3 twin rooms available
2 queen rooms available
No king rooms available
```

## TODO

- Complete `check_room_availability.py`

## Requirements

- The function should loop through each room type and check the availability of rooms based on the criteria described above.
- The function should print the availability of rooms for each room type.
