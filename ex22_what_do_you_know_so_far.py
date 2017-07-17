# Exercise 22: What Do You Know So Far?

# What Do You Know So Far?

# print()
print("Hello, let's go play with Python.")
print("Hens", 25.0 + 30.0 / 6.0)
print(3 + 2 < 5 - 7)
print("Is it greater?", 5 > -2)

cars = 100
print("There are", cars, "cars available.")

my_height = 180.7 # cm
print(f"He's {round(my_height)} cm tall.")

# left out assignment for types_of_people mentioned in intro
types_of_people = 10
# change variable from 10 to types_of_people
x =  f"There are {types_of_people} types of people" # it's called "f-string"
print(x)

# formatting using the .format() syntax when I want to apply a format to an already created string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

print("Its fleece was white as {}.".format('snow'))

w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removoing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end = " ")
print(end7 + end8 + end9 + end10 + end11 + end12)

formatter = "{} {} {} {}"
print(formatter.format("one", "two", "three", "four"))

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

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

# input()
# We put a end=' ' at the end of each print line. This tells print to not end the line with a newline character and go to the next line.
print("How old are you?", end=' ')
age = int(input())
print(f"So, you're {age} old.")

occupancy = input("What's your occupancy? ")
# print("What's your occupancy?", end= ' ')
# occupancy = input()
print(f"Occupancy: {occupancy}")

# argv
# add feature (the real name is MODULEs or libraries) to your script from the Python feature set
# We are importing the sys module
# Modules gives you features
from sys import argv # argv holds the arguments you pass to your Python script
# read the WYSS section for how to run this
script, first, second, third = argv # Take whatever is in argv, unpack it, and assign it to all of these variables on the left in order.
print("The script is called:", script)
print(f"Your first variable is: {first}")
print("Your second variable is:", second)
print("Your third variable is:", third)

# We'll use input slightly differently by having it print a simple > prompt
# We make a variable prompt that is set to the prompt we want, 
# and we give that to input instead of typing it over and over. 
# Now if we want to make the prompt something else, 
# we just change it in this one spot and rerun the script. Very handy.
from sys import argv
script, user_name, age = argv
prompt = '> Please answer: '
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
# combined a """ style multiline string with the {} format activator 
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice
""")

# Comment

# Reading Files
from sys import argv
# For now just understand that sys is a package, and this phrase just says to get the argv feature from that package.
script, filename = argv
txt = open(filename)
print(f"Here's your file {filename}")
print(txt.read()) # We are calling commands, but commands are also called functions or methods.
# "Hey txt! Do your read command with no parameters!"
# It's important to close files when you are done with them.
txt.close()

# Writing to the files
print("Opening the file...")
target = open(filename, 'w')  
# If you use 'w' then you're saying "open this file in 'write' mode," thus the 'w' character. There's also 'r' for "read," 'a' for append, and modifiers on these.
# The most important one to know for now is the + modifier, so you can do 'w+', 'r+', and 'a+'. This will open the file in both read and write mode, and depending on the character use position the file in different ways.
# 'r' (read) mode - the defalut for open() function
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
target.write(f"{line1}\n{line2}\n{line3}\n")
print("And finally, we close it.")
target.close()

# More Files
from sys import argv
from os.path import exists
# This returns True if a file exists, based on its name in a string as an argument. It returns False if not. 
# Using import is a way to get tons of free code other better (well, usually) programmers have written so you do not have to write it.
script, from_file, to_file = argv
indata = open(from_file).read()
print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()

# Functions
# Function checklist
# 1. Did you start your function definition with def?
# 2. Does your function name have only characters and _ (underscore) characters?
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
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Jan","Nemec")
print_two_again("Jan","Nemec")

# Functions and Files
def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline(), end= '')

current_line += 1
print_a_line(current_line, current_file)

# Functions Can Return Something
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

# python -m pydoc input
