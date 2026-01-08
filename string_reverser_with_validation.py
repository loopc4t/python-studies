"""
Goal: Write a program that asks for a string and prints it in reverse, but only if it’s a valid alphanumeric string.
Topics: String manipulation, input validation.
Challenge: Prompt the user to re-enter until they provide a valid alphanumeric string.
Tip: Use .isalnum() to check if a string is alphanumeric
"""

while True:
    
    string_to_reverse = input("Enter a string to reverse: ")


    if string_to_reverse.isalnum():
        reversed_string = string_to_reverse[::-1]
        print(reversed_string)
        break
    else:
        print("Please, try an alphanumeric string.\n")

    
    
