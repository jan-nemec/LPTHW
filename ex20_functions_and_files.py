# Exercise 20: Functions and Files

# Functions and Files

# Each time you do f.seek(0) you're moving to the start of the file. 
# Each time you do f.readline() you're reading a line from the file, 
# and moving the read head to right after the \n that ends that line. 
# This will be explained more as you go on.

from sys import argv

script, input_file = argv


def print_all(f):
	print(f.read())


def rewind(f):
	f.seek(0)


def print_a_line(line_count, f):
	print(line_count, f.readline(), end='')

# How does readline() know where each line is?
# Inside readline() is code that scans each byte of the file until it finds a \n character, 
# then stops reading the file to return what it found so far. 
# The file f is responsible for maintaining the current position in the file after each readline() call, 
# so that it will keep reading each line.

# The readline() function returns the \n that's in the file at the end of that line. 
# Add a end = "" at the end of your print function calls to avoid adding double \n to every line.

current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)