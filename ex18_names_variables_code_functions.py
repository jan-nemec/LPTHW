# Exercise 18: Names, Variables, Code, Functions

# Names, Variables, Code, Functions

# Functions do three things:
# They name pieces of code the way variables name strings and numbers.
# They take arguments the way your scripts take argv.
# Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."

# Function checklist
# 1. Did you start your function definition with def? Def introduces the function definition.
# Optional: """function's documentation or docstring - it's good practice to include docstrings"""
# 2. def is followed by the function name. Does your function name have only characters and _ (underscore) characters?
# 3. Did you put an open parenthesis ( right after the function name?
# 4. Did you put your arguments after the parenthesis ( separated by commas?
# 5. Did you make each argument unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon ): after the arguments?
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8. Did you "end" your function by going back to writing with no indent (dedenting we call it)?

# Call/Run/Use the Function
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parenthesis separated by commas?
# 4. Did you end the function call with a ) character?

# this one is like your scripts with argv
# That tells Python to take all the arguments to the function and then put them in args as a list. It's like argv that you've been using, but for functions. It's not normally used too often unless specifically needed.


def print_two(*args):  # put args as a list
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this


# Documentation Strings
def print_two_again(arg1, arg2):
    """Function's documentation or docstring - it's good practice to include docstrings."""
    # The first line should always be a short, concise summary of the object’s purpose.
    # This line should begin with a capital letter and end with a period.

    # If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description. 

    print(f"arg1: {arg1}, arg2: {arg2}")

print(print_two_again.__doc__)  # Get the Documentation Strings

# Function Annotations
# Function annotations are completely optional metadata information about the types used by user-defined functions 


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one has an default parameter eggs
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
# Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}

# default parameter
def simple(num1, num2 = 5):
    print(num1, num2)

simple(5)
simple(5, 555)


def print_none():
    print("I got nothing'.")


# The value of the function name can be assigned to another name which can then
# also be used as a function.
pn = print_none
pn()

print_two("Jan", "Nemec")
print_two_again("Jan", "Nemec")
print_one("First!")
print_none()

# Coming from other languages, you might object that print_two is not a function
# but a procedure since it doesn’t return a value.
# In fact, even functions without a return statement do return a value, albeit a rather boring one.
# This value is called None (it’s a built-in name).
# Writing the value None is normally suppressed by the interpreter if it would be the only value written.
# You can see it if you really want to using print():
print(print_two("Jan", "Nemec"))
