def check_room_availability(room_types, rooms_available):
    # This function checks the availability of different types of rooms and prints the corresponding message.

    # Loop through each room type in the list of room_types.
    for i in range(len(room_types)):
        # Check if there are 0 rooms available for a particular room type. if there are none, print "no <room type> rooms available".
        if rooms_available[i] == 0:
            print(f"No {room_types[i]} rooms available")
        # Check if there is one room available for a particular room type. if there's one, print "1 <room type> room available".
        elif rooms_available[i] == 1:
            print(f"1 {room_types[i]} room available")
        # Otherwise, print "<number of rooms available> <room type> rooms available".
        else:
            print(f"{rooms_available[i]} {room_types[i]} rooms available")
