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

print("And finally, we close it.")
target.close()

print("Would you like to output the new file?\nNO - CTRL-c\nYES - RETURN")

input("?")

target_again = open(filename, 'r')

print(target_again.read())

target_again.close()