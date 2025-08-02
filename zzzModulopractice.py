#This programme prompts the user to enter two whole numbers. It uses the decimal module to ensure accurate rounding. The first number can be any valid numeric input, while the second number must be non-zero to allow a modulo (%) calculation. If the user provides invalid input, the programme displays a message and asks again. Once both numbers are accepted, it performs the modulo operation and displays the result.


from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


# Convert user input to a rounded whole Decimal number:
def trying_the_number(user_input):
    try:
        return Decimal(user_input).to_integral_value(rounding=ROUND_HALF_UP)
    except InvalidOperation:
        print("That is not a valid number.")
        return None


# Repeatedly ask user for a number until valid input is given:
def game():
    while True:
        num = input("Enter a number: ")
        num_decimal = trying_the_number(num)
        if num_decimal is not None:
            return num_decimal


# Check that second number is not zero:
def second_var():
    while True:
        num_value = game()
        if num_value != 0:
            return num_value
        else:
            print("0 not allowed here.")


first_var = game()
second_var = second_var()

# Perform and display the modulo operation
print(f"{first_var}%{second_var}={first_var % second_var}")
