# Exercise 5: More Variables and Printing | f-Strings
"""More Variables and Printing"""

# Strings are really handy, so in this exercise you will learn how to make 
# strings that have variables embedded in them. 
# You embed variables inside a string by using a special {} sequence 
# and then put the variable you want inside the {} characters. 
# You also must start the string with the letter f for "format", 
# as in f"Hello {somevar}". This little f before the " (double-quote) 
# and the {} characters tell Python 3, 
# "Hey, this string needs to be formatted. Put these variables in there."

# Also called “formatted string literals,” f-strings are string literals that 
# have an f at the beginning and curly braces containing expressions that 
# will be replaced with their values. 
# The expressions are evaluated at runtime and 
# then formatted using the __format__ protocol.

# Python docs read more: 
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings

# Simple Syntax
my_name = 'Jan Nemec'
my_age = 38  # not a lie
my_height = 180  # cm
my_weight = 88  # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

inch = 0.393700787
pound = 2.20462262
my_height2 = my_height * inch
my_weight2 = round(my_weight * pound, 2)

print(f'Let\'s talk about {my_name}.')
print(f"He's {my_height} cm tall. It's {round(my_height2, 2)} inches.")
print(f"He's {my_weight} kg heavy. It's {my_weight2} pounds.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_weight + my_height
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# Arbitrary Expressions

# Because f-strings are evaluated at runtime, 
# you can put any and all valid Python expressions in them.
f"{2 * 37}"
# '74'

# You could also call functions.
def to_lowercase(input):
  return input.lower()

name = "Jan Nemec"
f"{to_lowercase(name)} is funny"

# You also have the option of calling a method directly:
f"{name.lower()} is funny"

# You could even use objects created from classes with f-strings.
class Comedian(object):
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __str__(self):
    return f"{self.first_name} {self.last_name} is {self.age}."

  def __repr__(self):
    return f"{self.first_name} {self.last_name} is {self.age}. Suprise!"

new_comedian = Comedian("Jan", "Nemec", 39)
f"{new_comedian}"
# The __str__() and __repr__() methods deal with how objects are presented as 
# strings, so you’ll need to make sure you include at least one of those 
# methods in your class definition. 
# If you have to pick one, go with __repr__() 
# because it can be used in place of __str__().

# The string returned by __str__() is the informal string representation of 
# an object and should be readable. The string returned by __repr__() 
# is the official representation and should be unambiguous. 
# Calling str() and repr() is preferable to using __str__() and __repr__() directly.

# By default, f-strings will use __str__(), but you can make sure 
# they use __repr__() if you include the conversion flag !r:
f"{new_comedian}"
f"{new_comedian!r}"

# Multiline f-strings
# But remember that you need to place an f in front of each line of a multiline string.
name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (
  f"Hi {name}."
  f"You are a {profession}."
  f"You were in {affiliation}."
)
message
# 'Hi Eric.You are a comedian.You were in Monty Python.'

# If you want to spread strings over multiple lines, 
# you also have the option of escaping a return with a \:
message = f"Hi {name}." \
          f"You are a {profession}." \
          f"You were in {affiliation}."
message
# 'Hi Eric.You are a comedian.You were in Monty Python.'

# But this is what will happen if you use """
message = f"""
  Hi {name}.
  You are a {profession}.
  You were in {affiliation}.
"""
# '\n  Hi Eric.\n  You are a comedian.\n  You were in Monty Python.\n'

# Speed
# The f in f-strings may as well stand for “fast.”
# f-strings are faster than both %-formatting and str.format().
# As you already saw, f-strings are expressions evaluated at runtime 
# rather than constant values. 
# At runtime, the expression inside the curly braces is evaluated 
# in its own scope and then put together with the string 
# literal part of the f-string. The resulting string is then returned. 
import timeit
timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000)

timeit.timeit("""name = "Eric"
age = 74
'{} is {}'.format(name, age)""", number= 10000)

timeit.timeit("""name = "Eric"
age = 74
f'{name} is {age}.'""", number= 10000)

# Python f-Strings: The Pesky Details

# Quotation Marks
f"{'Jan Nemec'}"
f'{"Jan Nemec"}'
# You can also use triple quotes:
f"""Jan Nemec"""
f'''Jan Nemec'''
f"The \"comedian\" is {name}, aged {age}."

# Dictionaries
# If you are going to use single quotation marks for the keys of the dictionary,
# then remember to make sure you’re using double quotation marks 
# for the f-strings containing the keys.
comedian = {'name': 'Jan Nemec', 'age': 39}
f"The comedian is {comedian['name']}, aged {comedian['age']}."

# Braces
f"{{74}}"
# {74}
f"{{{74}}}"
# {74}
f"{{{{74}}}}" # you can get more braces to show if you use more than triple braces.
# {{74}}

# Backslashes
# You can’t use backslashes to escape in the expression part of an f-string.
# f"{\"Eric Idle\"}" # SyntaxError: f-string expression part cannot include a backslash
# You can work around this by evaluating the expression beforehand and using the result in the f-string:
name = "Jan Nemec"
f"{name}"

# Inline Comments
# Expressions should not include comments using the # symbol. You will get a syntax error.
# f"Eric is {2 * 39 #Oh my!}." # SyntaxError: f-string expression part cannot include '#'


# "Old-school" String Formatting
# Before Python 3.6, you had two main ways of embedding Python expressions 
# inside string literals for formatting: 
# %-formatting 
#   and 
# str.format().

# Option #1: %-formatting

# Python docs read more: 
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
# Keep in mind that %-formatting is not recommended by the docs.

# String objects have a built-in operation using the % operator, 
# which you can use to format strings. 
name = "Jan"
"Hello, %s" % name

# In order to insert more than one variable, you must use a tuple of those variables. 
 "Hello, %s. You are %s." % (name, age)

# Why %-formatting Isn’t Great
# However, once you start using several parameters and longer strings, 
# your code will quickly become much less easily readable.
first_name = "Jan"
last_name = "Němec"
age = 39
profession = "expert"
affiliation = "Monty Python"
"Hello, %s %s. You are %s. You are an %s. You were a a member of %s." % (first_name, last_name, age, profession, affiliation)
# Unfortunately, this kind of formatting isn’t great because it is verbose 
# and leads to errors, like not displaying tuples or dictionaries correctly. 

# Option #2: str.format()

# Was introduced in Python 2.6
# Python docs read more: 
# https://docs.python.org/3/library/stdtypes.html#str.format

# With str.format(), the replacement fields are marked by curly braces:
"Hello, {}. You are {}".format(name, age)

# You can reference variables in any order by referencing their index:
"Hello, {1}. You are {0}".format(age, name)

# But if you insert the variable names, you get the added perk of being able 
# to pass objects and then reference parameters and methods in between the braces:
person = {'name': 'Jan', 'age': 39}
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])

# You can also use ** to do this neat trick with dictionaries:
# Tip
# If you had the variables you wanted to pass to .format() in a dictionary, 
# then you could just unpack it with .format(**some_dict) 
# and reference the values by key in the string.
"Hello, {name}. You are {age}.".format(**person)

# str.format() can still be quite verbose when you are dealing 
# with multiple parameters and longer strings.
print(("Hello, {first_name} {last_name}. You are {age}. " + 
       "You are a {profession}. You were a member of {affiliation}.") \
       .format(first_name=first_name, last_name=last_name, age=age, \
               profession=profession, affiliation=affiliation))

  # f-Strings
  # They joined the party in Python 3.6           