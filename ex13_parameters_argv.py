# Exercise 13: Parameters, Unpacking, Variables
# Run shell commands
# You know how you type python ex13.py to run the ex13.py file?
# Well the ex13.py part of the command is called an ”argument.” 

# Add feature (the real name is MODULEs or libraries) to your script from the Python feature set
# We are importing the sys module
# Modules gives you features

# Called an ”import.” This is how you add features to your script from the Python
# feature set. Rather than give you all the features at once, Python asks you to say what you plan to use.
# This keeps your programs small, but it also acts as documentation for other programmers who read your
# code later.
from sys import argv  # argv holds the arguments you pass to your Python script
# Argument passing - the script name and additional arguments thereafter are
# turned into a list of strings and assigned to the arg variable in the sys module.
# The length of the list is at least one; when no script and no arguments are
# given, sys.argv[0] is is an empty string.

script, first, second, third = argv
# ”unpacks” argv so that, rather than holding all the arguments, 
# it gets assigned to four variables you can work with: script, first, second, and third. 
# Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.
# The command line arguments are strings - Use int() to convert them just like with int(input())

print("The script is called:", script)
print(f"Your first variable is: {first}")
print("Your second variable is:", second)
# print("Your third variable is:", third)
print("Your third variable is: {}".format(third))

# python ex13_parameters_argv.py first 2nd 3rd


age = input("How old are you? ")
print(f'You are {age} old.')
# What’s the difference between argv and input()? The difference has to do with where the user is re-
# quired to give input. If they give your script inputs on the command line, then you use argv. If
# you want them to input using the keyboard while the script is running, then use input().
print(f'In ten years you will be {int(age) + 10} old.')

# Converting Strings to Numbers
int("12")
# 12
float("12")
# 12.0

num = input("Enter a number to be doubled: ")
doubled_num = float(num) * 2
print(doubled_num)