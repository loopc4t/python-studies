"""
Goal: Write a program that takes two numbers and an arithmetic operation (+, -, *, or /) and outputs the result.
Topics: Variables, input/output, conditionals, arithmetic operators.
Challenge: Add error handling for invalid inputs, like non-numeric inputs or division by zero.
Tip: Use if statements to validate the operation and handle the case when the user tries to divide by zero.
"""

while True:

    try:

        number_1 = int(input("\nType a number: "))
        operation = input("Choose an operation (+, -, *, or /): ")
        number_2 = int(input("Type another number: "))
        
        if operation == "+":
            print(f"{number_1} {operation} {number_2} = {number_1 + number_2}")

        elif operation == "-":
            print((f"{number_1} {operation} {number_2} = {number_1 - number_2}"))

        elif operation == "*":
            print((f"{number_1} {operation} {number_2} = {number_1 * number_2}"))

        elif operation == "/":
            if number_2 == 0:
                print("\nYou cannot divide by zero. Please try again")
            else:
                print((f"{number_1} {operation} {number_2} = {number_1 / number_2}"))

        else:
            print("\nPlease use a valid operator.")

    except ValueError:
        print("That was not a valid number!")
