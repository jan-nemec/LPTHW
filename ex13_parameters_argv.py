# Exercise 13: Parameters, Unpacking, Variables
# Run shell commands

# Add feature (the real name is MODULEs or libraries) to your script from the Python feature set
# We are importing the sys module
# Modules gives you features

# Called an ”import.” This is how you add features to your script from the Python
# feature set. Rather than give you all the features at once, Python asks you to say what you plan to use.
# This keeps your programs small, but it also acts as documentation for other programmers who read your
# code later.
from sys import argv  # argv holds the arguments you pass to your Python script

script, first, second, third = argv  # Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.

print("The script is called:", script)
print(f"Your first variable is: {first}")
print("Your second variable is:", second)
# print("Your third variable is:", third)
print("Your third variable is: {}".format(third))

# python ex13_parameters_argv.py first 2nd 3rd
