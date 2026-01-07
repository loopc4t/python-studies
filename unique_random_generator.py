import random

""""
Goal: Write a function that returns a list of n unique random digits from 0 to 9.
Topics: Lists, randomization, loops.
Challenge: Modify the function to generate unique random numbers within any specified range.
Tip: Use random.sample() to simplify the process of selecting unique digits.
"""

try:

    unique_digits = int(input("Enter the number of unique digits you want (1-10): "))
    unique_numbers = range(0, 9)

    def unique_random_number_generator():
        random_number = random.sample(unique_numbers, k=unique_digits)
        print(f"Unique random digits: {random_number}")


    unique_random_number_generator()

except ValueError:
    print("Please enter the correct number of digits.")

