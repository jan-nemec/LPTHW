# Exercise 9: Printing, Printing, Printing
"""Printing, Printing, Printing"""

from textwrap import dedent  # ex43

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print(dedent("""
    There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.
"""))

# Input and Output
# Fancier Output Formatting

# The string type has some methods that perform useful operations for padding 
# strings to a given column width; these will be discussed shortly. 
# The second way is to use formatted string literals, or the str.format() method.

# (The string module contains a Template class which offers yet another way to
# substitute values into strings.)

# How do you convert values to strings? 
# Luckily, Python has ways to convert any value to a string: 
# pass it to the repr() or str() functions.

# The str() function is meant to return representations of values which are
# fairly human-readable, while repr() is meant to generate representations
# which can be read by the interpreter 

# str() - converting numbers to strings
num_pancakes = 10
"I am going to eat " + str(num_pancakes) + " pacakes."

s = 'Hello, world.'
str(s)
# 'Hello, world.'
repr(s)
# "'Hello, world.'"
str(1/7).rjust(10) #str.ljust() str.center()
# This example demonstrates the str.rjust() method of string objects, 
# which right-justifies a string in a field of a given width by padding it with spaces on the left. 

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# There is another method, str.zfill(), 
# which pads a numeric string on the left with zeros. 
# It understands about plus and minus signs:
'12'.zfill(5)
'-3.14159265359'.zfill(5)