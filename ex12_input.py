# Exercise 12: Prompting People
# python -m pydoc input

# To use the input() function, you must specify a prompt. The prompt is just
# a string that you put in between the parentheses of input(). The input()
# function displays the prompt and waits for the user to type something on
# their keyboard. When the user hit Enter, input() returns their input as a
# string that can be assigned to a variable.

occupancy = input("What's your occupancy? ")
# print("What's your occupancy?", end= ' ')
# occupancy = input()

print(f"Zaměstnání: {occupancy}")

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")