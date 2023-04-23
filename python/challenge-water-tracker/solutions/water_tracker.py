def record_water_intake(water_tracker, new_intake):
    # This function records the water intake at a certain time and returns the total amount consumed so far for a given day.

    # Split the input tuple (new_intake) into two values - time and amount
    time, amount = new_intake

    # Check if the input time already exists in the dictionary. if it does, add the new water intake to the existing amount.
    # If it doesn't, create a new entry with the input time and add the input intake amount.
    if time in water_tracker:
        water_tracker[time] += amount
    else:
        water_tracker[time] = amount

    # Use python's built-in sum() function to calculate the total intake for the current day by adding all values in the dictionary.
    total_intake = sum(water_tracker.values())

    # Return the total intake for the current day.
    return total_intake
