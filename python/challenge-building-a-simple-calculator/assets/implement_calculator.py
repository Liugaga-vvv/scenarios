from simple_calculator import simple_calculator

calculator = simple_calculator()
print("Welcome to the Simple Calculator Program!")
print("------------------------------------------")
while True:
    num1, num2, operation = calculator.get_user_input()
    message = calculator.validate_user_input(num1, num2, operation)
    if message != None:
        continue
    result = calculator.perform_calculation(num1, num2, operation)
    calculator.display_result(result)
    answer = input("Do you want to perform another calculation? (Y/N):")
    if answer == "N":
        break
print("Thank you for using the Simple Calculator Program!")
