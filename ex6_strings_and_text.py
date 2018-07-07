# Exercise 6: Strings and Text
"""Strings and Text"""

# left out assignment for types_of_people mentioned in intro
types_of_people = 10
# change variable from 10 to types_of_people
x =  f"There are {types_of_people} types of people."  # it's called "f-string"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# left out f in front of string and omit extra period
print(f"I said: {x}")
# left out f in front of string and omit extra period
print(f"I also said: '{y}'")

# formatting using the .format() syntax 
# You'll see me use that sometimes when I want to apply a format 
# to an already created string, such as in a loop.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# change "What You Should See" snapshot to reflect changes

# The string is enclosed in double quotes if the string contains a single quote 
# and no double quotes, otherwise it is enclosed in single quotes. 
# The print() function produces a more readable output, 
# by omitting the enclosing quotes and by printing escaped and special characters:
'"Isn\'t," she said.'
print('"Isn\'t," she said.')
