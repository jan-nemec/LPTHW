# Exercise 16: Reading and Writing Files

# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.
# seek(0) -- Move the read/write location to the beginning of the file.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
# target = open(filename, 'w+')
# If you use 'w' then you're saying "open this file in 'write' mode," thus the 'w' character. There's also 'r' for "read," 'a' for append, and modifiers on these.
# The most important one to know for now is the + modifier, so you can do 'w+', 'r+', and 'a+'. This will open the file in both read and write mode, and depending on the character use position the file in different ways.
# 'r' (read) mode - the defalut for open() function
# 'w' for only writing (an existing file with the same name will be erased)

# 'b' appended to the mode opens the file in binary mode: 
# now the data is read and written in the form of bytes objects. 
# This mode should be used for all files that don’t contain text.
# In text mode, the default when reading is to convert platform-specific line 
# endings (\n on Unix, \r\n on Windows) to just \n. 
# When writing in text mode, the default is to convert occurrences of \n back 
# to platform-specific line endings. 
# This behind-the-scenes modification to file data is fine for text files, 
# but will corrupt binary data like that in JPEG or EXE files. Be very careful 
# to use binary mode when reading and writing such files.

# It is good practice to use the with keyword when dealing with file objects. 
# The advantage is that the file is properly closed after its suite finishes, 
# even if an exception is raised at some point. Using with is also much shorter 
# than writing equivalent try-finally blocks:
with open('workfile') as f:
    read_data = f.read()
f.closed

# If you’re not using the with keyword, 
# then you should call f.close() to close the file and immediately 
# free up any system resources used by it.

# To read a file’s contents, call f.read(size), 
# which reads some quantity of data and returns it as a string (in text mode) 
# or bytes object (in binary mode). 
# size is an optional numeric argument. 
# When size is omitted or negative, 
# the entire contents of the file will be read and returned;
 # If the end of the file has been reached, f.read() will return an empty string ('').
f.read()
# 'This is the entire file.\n'
f.read()
# '' # f 
# f.readline() returns an empty string, the end of the file has been reached

# If you want to read all the lines of a file in a list you can also use 
# list(f) 
# or 
# f.readlines().

# For reading lines from a file, you can loop over the file object. 
# This is memory efficient, fast, and leads to simple code:
for line in f:
    print(line, end='')

print("Truncating the file. Goodbye!")
target.truncate()
# print(target.read())

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(f"{line1}\n{line2}\n{line3}\n")

# f.write(string) writes the contents of string to the file, 
# returning the number of characters written.
print("And finally, we close it.")
target.close()

print("Would you like to output the new file?\nNO - CTRL-c\nYES - RETURN")

input("?")

target_again = open(filename, 'r')

print(target_again.read())

# f.tell() returns an integer giving the file object’s current position
# in the file represented as number of bytes from the beginning of the file 
# when in binary mode and an opaque number when in text mode.

# To change the file object’s position, use f.seek(offset, from_what).
# The position is computed from adding offset to a reference point; 
# the reference point is selected by the from_what argument. 
# A from_what value of 
#   0 measures from the beginning of the file, 
#   1 uses the current file position, and 
#   2 uses the end of the file as the reference point. 
# from_what can be omitted and defaults to 0, 
# using the beginning of the file as the reference point.
f = open('ex16_test.txt', 'rb+')
f.seek(5) # Go to the 6th byte in the file
f.seek(-3, 2)  # Go to the 3rd byte before the end

# In text files (those opened without a b in the mode string), 
# only seeks relative to the beginning of the file are allowed 
#  and the only valid offset values are those returned from the f.tell(), or zero.

target_again.close()

