# Exercise 17: More Files

# More Files
from sys import argv
from os.path import exists
# This returns True if a file exists, based on its name in a string as an argument. It returns False if not.
# Using import is a way to get tons of free code other better (well, usually) programmers have written so you do not have to write it.

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We coud do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()
# which means you don't need to then do in_file.close() when you reach the end of the script. It should already be closed by Python once that one line runs.

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
# in_file.close()