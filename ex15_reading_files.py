# Exercise 15: Reading Files

# Reading Files
# We want to do is ”open” that file in our script and print it ou
# However, we do not want to just "hard code" the name ex15_sample.txt into our script.
# "Hard coding" means putting some bit of information that should come from the user
# as a string directly in our source code. That's bad because we want it to load other files later.
# The solution is to use argv or input to ask the user what file to open
# instead of "hard coding" the file's name.
from sys import argv
# For now just understand that sys is a package (Module), and this phrase just says to get the argv feature from that package.

script, filename = argv

txt = open(filename)
# Does txt = open(filename) return the contents of the file? No, it doesn’t. It actually makes some-
# thing called a ”file object.”
# open() returns a file object, and is most commonly used with two arguments: 
# open(filename, mode).
# The file object is not the file’s contents

print(f"Here's your file {filename}")
print(txt.read()) # We are calling commands, but commands are also called functions or methods.
# "Hey txt! Do your read command with no parameters!"
# It's important to close files when you are done with them.

txt.close()

print("Type the filename again: ", end=" ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt_again.close()