# Exercise 6: Strings and Text
"""Strings and Text"""

# Strings are one of the fundamental Python data types (str). The term data type 
# refers to what kind of data a value represents. Strings are used to represent
# test. We say that strings are fundamental data type because they can't be 
# broken down into smaller values of a different type.

type("Hello, world!")
# <class 'str'>
# The output <class 'str'> indicatas that the value "Hello, world" is an
# instance of the str data type.

# left out assignment for types_of_people mentioned in intro
types_of_people = 10
# change variable from 10 to types_of_people
x =  f"There are {types_of_people} types of people."  # it's called "f-string"

binary = "binary" # string literal
# Whenever you create a string by surrounding text with quotation marks,
# the string is called a string literal. The name indicates that the string
# is literally written out in your code.

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

# Strings can be concatenated (glued together) with the + operator, 
# and repeated with *:
3 * 'un' + 'ium'

# Two or more string literals (i.e. the ones enclosed between quotes) 
# next to each other are automatically concatenated.
'Py' 'thon'
# This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')

print(w + e)

# change "What You Should See" snapshot to reflect changes

# String Indexing
# Each character in a string has a numbered position called an index.
flavor = "apple pie"
flavor[1]
# Getting the final character with the index -1 taks less typing and
# doesn't require an intermediate step to calculate the final index:
flavor[-1]
final_index = len(flavor) - 1
last_character = flavor[final_index]




# The string is enclosed in double quotes if the string contains a single quote 
# and no double quotes, otherwise it is enclosed in single quotes. 
# The print() function produces a more readable output, 
# by omitting the enclosing quotes and by printing escaped and special characters:
'"Isn\'t," she said.'
print('"Isn\'t," she said.')

# The Length of a String
len("abc")

letters = "abc"
num_letters = len(letters)
num_letters

# Multiline Strings

# PEP 8 recommends 79-character line-length because, among other things,
# it makes it easier to read two files side-by-side.

# To deal with long strings, you can break the string up across multiple
# lines int a multiline string.
# One way is to break the string up across multiple lines and put a backslash
# \ at the and of  all but the last line.
paragraph = "This planet has - or rather had - a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem."
print(paragraph)
# When you print() a multiline string that is broken up by backslashes,
# the output displayed on a singlie line.

# Multiline strings can also be created using triple quotes as delimiter
# """ or '''
paragraph = """This planet has - or rather had - a problem, which was
        this: most of the people living on it were unhappy for pretty much
                of the time. Many solutions were suggested for this problem."""
# Triple-quoted strings preserve whitespace.
print(paragraph)
