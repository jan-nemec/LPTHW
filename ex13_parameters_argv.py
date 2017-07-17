# Exercise 13: Parameters, Unpacking, Variables

# add feature (the real name is MODULEs or libraries) to your script from the Python feature set
# We are importing the sys module
# Modules gives you features
from sys import argv  # argv holds the arguments you pass to your Python script
# read the WYSS section for how to run this
script, first, second, third = argv  # Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.

name = input('What\'s your name? ')
print("Hello,", name)

print("How old are you?", end=" ")
age = input()
print("You are", age, "old.")

print("The script is called:", script)
print(f"Your first variable is: {first}")
print("Your second variable is:", second)
# print("Your third variable is:", third)
print("Your third variable is: {}".format(third))

# python ex13_parameters_argv.py first 2nd 3rd
