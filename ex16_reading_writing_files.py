# Exercise 16: Reading and Writing Files

# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.
# seek(0) -- Move the read/write location to the beginning of the file.

# .read(size=-1) 
# This reads from the file based on the number of size bytes. 
# If no argument is passed or None or -1 is passed, then the entire file is read.

# .readline(size=-1) 
# This reads at most size number of characters from the line. 
# This continues to the end of the line and then wraps back around. 
# If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.

# .readlines() 
# This reads the remaining lines from the file object and returns them as a list.

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
# 'w' for only writing (an existing file with the same name will be erased) -> Open for writing, truncating (overwriting) the file first

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

# 'r' Open for reading (default)
# 'rb' or 'wb' Open in binary mode (read/write using byte data)

# When you’re manipulating a file, there are two ways that you can use to ensure 
# that a file is closed properly, even when encountering an error. 
# The first way to close a file is to use the try-finally block:
reader = open(filename)
try:
    # Further file processing goes here
finally:
    reader.close()

# The second way to close a file is to use the with statement:
# It is good practice to use the with keyword when dealing with file objects. 
# The advantage is that the file is properly closed after its suite finishes, 
# even if an exception is raised at some point. Using with is also much shorter 
# than writing equivalent try-finally blocks.
 # I highly recommend that you use the with statement as much as possible, 
 # as it allows for cleaner code and makes handling any unexpected errors easier for you.
with open('workfile') as f:
    read_data = f.read()
f.closed # return True if file is closed

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
# You should always make sure that an open file is properly closed.
# In most cases, upon termination of an application or script, a file will be closed eventually. 
# However, there is no guarantee when exactly that will happen. 
# This can lead to unwanted behavior including resource leaks. 
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

# There are three different categories of file objects:
# Text files
# Buffered binary files
# Raw binary files

# Text File Types
file = open('ex15_sample.txt')
type(file)

# Buffered Binary File Types
file = open('ex15_sample.txt', 'rb')
type(file)
file = open('ex15_sample.txt', 'wb')
type(file)

# Raw File Types
# A raw file type is: “generally used as a low-level building-block for binary and text streams.” 
# It is therefore not typically used.
file = open('ex15_sample.txt', 'rb', buffering=0)
type(file)

# Iterating Over Each Line in the File

with open('ex15_sample.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '': # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

# Another way you could iterate over each line in the file is to use 
# the .readlines() of the file object. 
# Remember, .readlines() returns a list where each element 
# in the list represents a line in the file:
with open('ex15_sample.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

# However, the above examples can be further simplified by iterating over 
# the file object itself:
with open('ex15_sample.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')
# This final approach is more Pythonic and can be quicker and more memory efficient. 

# Writing
#.write(string) - This writes the string to the file.
#.writelines(seq) - This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

with open('ex15_sample.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()

with open('ex15_sample_reveresed.txt', 'w') as writer:
    # Alternatively you can use writer.writelines(reversed(dog_breeds))

    # Write to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)

# Working With Bytes
# Sometimes, you may need to work with files using byte strings. 
# This is done by adding the 'b' character to the mode argument. 
# All of the same methods for the file object apply. 
# However, each of the methods expect and return a bytes object instead:
with open('ex15_sample.txt', 'rb') as reader:
    print(reader.readline())

with open('jack_russell.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))


    


