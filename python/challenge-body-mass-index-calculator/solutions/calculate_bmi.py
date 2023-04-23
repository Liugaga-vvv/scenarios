# define a function called "calculate_bmi" which takes two parameters, weight and height.
def calculate_bmi(weight, height):
    # calculate the bmi using the formula weight divided by height squared.
    bmi = weight / (height * height)
    # round the calculated bmi value to two decimal places using the built-in round function.
    return round(bmi, 2)
