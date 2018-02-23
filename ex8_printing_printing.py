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