# Exercise 16: Reading and Writing Files

# close -- Closes the file. Like File->Save.. in your editor.
# read -- Reads the contents of the file. You can assign the result to a variable.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. Watch out if you care about the file.
# write('stuff') -- Writes "stuff" to the file.
# seek(0) -- Move the read/write location to the beginning of the file.


# Reading and Writing Opened Files

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
# When you want to work with a file, the first thing to do is to open it. 
# This is done by invoking the open() built-in function. 
# open() has a single required argument that is the path to the file. 
# open() has a single return, the file object:
target = open(filename, 'w')

# Most likely, you’ll also want to use the second positional argument, mode. 
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

# Warning: You should always make sure that an open file is properly closed.

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

with open('ex15_sample.txt', 'r') as f:
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)


# In text files (those opened without a b in the mode string), 
# only seeks relative to the beginning of the file are allowed 
#  and the only valid offset values are those returned from the f.tell(), or zero.

target_again.close()


# There are three different categories of file objects:
# Text files
# Buffered binary files
# Raw binary files

# Text File Types
file = open('ex15_sample.txt', 'r')¨
# With these types of files, open() will return a TextIOWrapper file object:
type(file)

# Buffered Binary File Types
# With these types of files, open() will return either a BufferedReader or BufferedWriter file object:
file = open('ex15_sample.txt', 'rb')
type(file)
file = open('ex15_sample.txt', 'wb')
type(file)

# Raw File Types
# A raw file type is: “generally used as a low-level building-block for binary and text streams.” 
# It is therefore not typically used.
file = open('ex15_sample.txt', 'rb', buffering=0)
# With these types of files, open() will return a FileIO file object:
type(file)


# Examples of how to use .read(), .readline(), .readlines() methods.
with open('dog_breeds.txt') as reader:
    print(reader.read())

# How to raead 5 bytes of a line using .readline()
with open('dog_breeds.txt') as reader:
    print(reader.readline(5))
    # Notice that line is greater than the 5 chars and continues
    # down the line, reading 5 chars each time until the end of the
    # line and then "wraps" around
    print(reader.readline(5))
    print(reader.readline(5))

# how to read the entire file as a list using the Python .readlines() method
with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()


# Iterating Over Each Line in the File

with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    line = reader.readline()
    while line != '': # The EOF char is an empty string
        print(line, end='')
        # The end='' is to prevent Python from adding an additional newline 
        # to the text that is being printed and only print what is being read from the file.
        line = reader.readline()

# Another way you could iterate over each line in the file is to use 
# the .readlines() of the file object. 
# Remember, .readlines() returns a list where each element 
# in the list represents a line in the file:
with open('dog_breeds.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end='')

# Pythonic
# However, the above examples can be further simplified by iterating over 
# the file object itself:
with open('dog_breeds.txt', 'r') as reader:
    # Read and print the entire file line by line
    for line in reader:
        print(line, end='')
# This final approach is more Pythonic and can be quicker and more memory efficient. 


# Storing text data in a list variable
my_lines = []
with open('dog_breeds.txt', 'rt') as reader:
    for line in reader:
        my_lines.append(line)
    
    # A list object is an iterator, so to print every element of the list, we can
    # iterate over it with for...in:
    for my_line in my_lines:
        print(my_line, end='')
print(my_lines)

# v2 with rstrip()
my_lines = []
with open('dog_breeds.txt', 'rt') as reader:
    for line in reader:
        my_lines.append(line.rstrip('\n'))
    
    # A list object is an iterator, so to print every element of the list, we can
    # iterate over it with for...in:
    for my_line in my_lines:
        print(my_line)

# Writing
#.write(string) - This writes the string to the file.
#.writelines(seq) - This writes the sequence to the file. 
    # - No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')

with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()

with open('dog_breeds_reveresed.txt', 'w') as writer:
    # Alternatively you can use writer.writelines(reversed(dog_breeds))

    # Write to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)

# Working With Bytes
# Sometimes, you may need to work with files using byte strings. 
# This is done by adding the 'b' character to the mode argument. 
# All of the same methods for the file object apply. 
# However, each of the methods expect and return a bytes object instead:
with open('dog_breeds.txt', 'rb') as reader:
    print(reader.readline())

with open('jack_russell.png', 'rb') as byte_reader:
    print(byte_reader.read(1))
    print(byte_reader.read(3))
    print(byte_reader.read(2))
    print(byte_reader.read(1))
    print(byte_reader.read(1))


# Appending to a File
# Sometimes, you may want to append to a file or start writing at the end 
# of an already populated file. This is easily done by using the 'a' character
# for the mode argument:
with open('dog_breeds.txt', 'a') as a_writer:
    a_writer.write('\nBeagle')


# Working With Two Files at the Same Time
# You may want to read a file and write to another file at the same time.
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))


with open('ex15_sample.txt', 'r') as rf:
    with open('test2.txt', 'w') as wf: # These 2 open statements can be written on a single line
        # Two lines -> better readibility (Corey Schafer)
        for line in rf:
            wf.write(line)


# Copy a large picture file
# binary mode - add 'b' -> 'rb'/'wb'
with open('jack_russell.png', 'rb') as rf:
    with open('jack_russell_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)


# In specific chunk sizes
with open('jack_russell.png', 'rb') as rf:
    with open('jack_russell_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# How to extract specific portions of a text file using Python

# Finding all occurrences of a substring
# We can iterate over the string, starting from the index of the previous match.

# When an occurrence is found, we call find again, starting from a new location in the string.
my_lines = []
with open('ex15_sample.txt') as rf:
    for line in rf:
        my_lines.append(line.rstrip('\n'))

# Locate and print all occurences of letter "e"
index = 0
prev = 0
phrase = my_lines[5]
substr = 'e'
while index < len(phrase):
    index = phrase.find(substr, index)
    if index == -1:
        break
    print(" " * (index - prev) + substr, end='')
    prev = index + len(substr)
    index += len(substr)

print(str)
#print('\n' + str)

# Incorporating regular expressions
import re
phrase = "Good morning, Doctor."
pattern = re.compile(r"\bd\w*r\b", re.IGNORECASE)
if pattern.search(phrase) != None:
    print("Found it.")

# Printing all lines containing substring
errors = []
linenum = 0
substr = "error".lower()
with open("logfile.txt", "rt") as rf:
    for line in rf:
        linenum += 1
        if line.lower().find(substr) != -1:
            errors.append("Line " + str(linenum) + ": " + line.rstrip('\n'))
for err in errors:
    print(err)

# Extract all lines containing substring, using regex
# The program below is similar to the above program, 
# but using the re regular expressions module. 
# The errors and line numbers are stored as tuples, e.g., (linenum, line).
import re
filename = 'logfile.txt'
errors = []
linenum = 0
pattern = re.compile("error", re.IGNORECASE)
with open(filename, 'rt') as rf:
    for line in rf:
        linenum += 1
        if pattern.search(line) != None:
            errors.append((linenum, line.rstrip('\n')))
for err in errors:
    print("Line " + str(err[0]) + ": " + err[1])

