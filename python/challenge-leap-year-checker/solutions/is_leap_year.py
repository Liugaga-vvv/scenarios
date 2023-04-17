# This function takes a year as a parameter and returns True if it is a leap year, False otherwise.
def is_leap_year(year):
    # Check if the year is divisible by 4.
    if year % 4 == 0:
        # If it is, check if it is also divisible by 100.
        if year % 100 == 0:
            # If it is, check if it is also divisible by 400.
            if year % 400 == 0:
                # If it is, it is a leap year, so return True.
                return True
            else:
                # If it is not divisible by 400, it is not a leap year, so return False.
                return False
        else:
            # If it is not divisible by 100, but it is divisible by 4, it is a leap year, so return True.
            return True
    else:
        # If it is not divisible by 4, it is not a leap year, so return False.
        return False
