# Exercise 10: What Was That?
"""Escape Sequences"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

escape_sequence = "My\nname is \n\t\\/\"John\"\\/"
print(escape_sequence)

print("I am 6'2\" tall.")
print('I am 6\'2" tall.')

# If you don’t want characters prefaced by \ to be interpreted as special 
# characters, you can use raw strings by adding an r before the first quote:
print(r'C:\some\name')
