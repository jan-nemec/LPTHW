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
<<<<<<< HEAD
print("Python")
=======
# Then the initial newling is not included.
>>>>>>> 76620df7e7867958ab8fd17d93c351f9d4663a37
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Strings can be concatenated with the + operator, and repeated with *:
3 * 'un' + 'im'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
'Py' 'thon'

# This feature is particularly useful when you want to break long strings:
# This only works with two literals though, not with variables or expressions:
text = ('Put several strings within parentheses '
        'to have them joined together.')

<<<<<<< HEAD
# if you want to concatenate variables or a variable and a literal, use +:
prefix = 'Py'
prefix + 'thon'

=======
# Strings can be indexed (subscripted), with the first character having index 0
>>>>>>> 76620df7e7867958ab8fd17d93c351f9d4663a37
word = 'Python'
word[0]
word[0:2]  # characters from position 0 (included) to 2 (excluded)
# This makes sure that s[:i] + s[i:] is always equal to s:
word[:2] + word[2:]
# Slice indices have useful defaults; an omitted first index defaults to zero, 
# an omitted second index defaults to the size of the string being sliced.

# If you omit both the first and second numbers in a slice, it returns the
# entire string.
word[:]
# Python


# Indices may also be negative numbers, to start counting from the right
word[-1]  # last character
# Note that since -0 is the same as 0, negative indices start from -1.

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

# Strings Are Immutable

# Python strings cannot be changed once you've created them — they are immutable. 
# Therefore, assigning to an indexed position in the string results in an error:
# word[0] = 'J'
# If you need a different string, you should create a new one:
'J' + word[1:]

# The built-in function len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
len(s)

# String Methods
# https://docs.python.org/3/library/stdtypes.html#string-methods

# Converting String Case
"Jean-luc Pickard".lower()
# the dot (.) tells Python that what follows is the name of a method - the
# lower() method in this case.

"Jean-luc Pickard".upper()

# Removing Whitespace From a String
name = "Jean-luc Picard      "
name.rstrip()

"123abc".rstrip("bc")
# The statement string.rstrip('\n') will strip a newline character from the right side of string. 
'Lorem Ipsum\n'.rstrip('\n')

name = "         Jean-luc Picard"
name.lstrip()

name = "     Jean-luc Picard    "
name.strip()

# Determine if a String Starts or Ends With a Particular String
starship = "Enterprise"
starship.startswith("en")
starship.endswith("rise")

# Find a String in a String
phrase = "the surprise is in here somewhere"
phrase.find("surprise")
# If .find() doesn’t ﬁnd the desired substring, it will return -1 instead.
# .find() only returns the index of the ﬁrst occurrence of a substring

# The find() method takes two optional, additional parameters: a start index and a stop index:
phrase = "I'm telling you the truth; nothing but the truth!"
# If stop is not specified, find() starts at index start, and stops at the end of the string.
print(phrase.find('e', 10))

# .replace() 
my_story = "I'm telling you the truth; nothing but the truth!"
my_story.replace("the truth", "lies")

# .replace() can only replace one substring at a time, so if you want to
# replace multiple substrings in a string you need to use .replace() mul-
# #tiple times:
text = "some of the stuff"
new_text = text.replace("some of", "all")
new_text = new_text.replace("stuff", "things")
new_text