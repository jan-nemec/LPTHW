# Exercise 8: Printing, Printing
"""Printing, Printing"""

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("I had this thing.",
					   "That you could type up right.",
					   "But it didn't sing.",
					   "So I said goodnight."))

# The brackets and characters within them (called format fields) are replaced 
# with the objects passed into the str.format() method. 
# A number in the brackets can be used to refer to the position of the object 
# passed into the str.format() method.
print('{4} {3} {2} {1}'.format(4, 3, 2, 1)

# If keyword arguments are used in the str.format() method, 
# their values are referred to by using the name of the argument.
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# Positional and keyword arguments can be arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# An optional ':' and format specifier can follow the field name. 
# This allows greater control over how the value is formatted. 
import math
print('The value of PI is approximately {0:.3f}'.format(math.pi))

# Passing an integer after the ':' will cause that field to be a minimum number
# of characters wide. This is useful for making tables pretty.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
        print('{0:10} ==> {1:10d}'.format(name, phone))

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used 
# to convert the value before it is formatted:
contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
# My hovercraft is full of eels.
print('My hovercraft is full of {!r}.'.format(contents))
# My hovercraft is full of 'eels'.

# It would be nice if you could reference the variables to be formatted by name
# instead of by position. 
# This can be done by simply passing the dict and using square brackets '[]' to access the keys.math

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# This could also be done by passing the table as keyword arguments 
# with the ‘**’ notation.
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# Old string formatting
import math
print('The value of PI is approximately %5.3f.' % math.pi)
# The value of PI is approximately 3.142.

# End of lines are automatically included in the string, 
# but it’s possible to prevent this by adding a \ at the end of the line.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
'Py' 'thon'

# This feature is particularly useful when you want to break long strings:
# This only works with two literals though, not with variables or expressions:
text = ('Put several strings within parentheses '
        'to have them joined together.')

word = 'Python'
word[0:2]  # characters from position 0 (included) to 2 (excluded)
# This makes sure that s[:i] + s[i:] is always equal to s:
word[:2] + word[2:]

# Python strings cannot be changed — they are immutable. 
# Therefore, assigning to an indexed position in the string results in an error:
# word[0] = 'J'
# If you need a different string, you should create a new one:
'J' + word[1:]
