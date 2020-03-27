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

# Study Drills
# See how short you can make the script. I could make this one line long.
in_file = open(to_file, 'w').write(open(from_file).read())
in_file.close()
# When I try to make this script shorter I get an error when I close the files at the end. 
# You probably did something like this, indata = open(from_file).read(), which means you don’t need to then
# do in_file.close() when you reach the end of the script. It should already be closed by Python
# once that one line runs.

# Line Endings

# The line ending has its roots from back in the Morse Code era, 
# when a specific pro-sign was used to communicate the end of a transmission or the end of a line.
# The American Standards Association (ASA) tates that line endings should use 
# the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n).
# The ISO (The International Organization for Standardization) standard however allowed 
# for either the CR+LF characters or just the LF character.

# Windows uses the CR+LF characters to indicate a new line, 
# while Unix and the newer Mac versions use just the LF character.

# Character Encodings
# Another common problem that you may face is the encoding of the byte data.
# The two most common encodings are the ASCII and UNICODE Formats. 
# ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

# ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values.