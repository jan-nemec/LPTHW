# Exercise 15: Reading Files

# Reading Files
# However, we do not want to just "hard code" the name ex15_sample.txt into our script.
# "Hard coding" means putting some bit of information that should come from the user
# as a string directly in our source code. That's bad because we want it to load other files later.
# The solution is to use argv or input to ask the user what file to open
# instead of "hard coding" the file's name.
from sys import argv
# For now just understand that sys is a package, and this phrase just says to get the argv feature from that package.

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read()) # We are calling commands, but commands are also called functions or methods.
# "Hey txt! Do your read command with no parameters!"
# It's important to close files when you are done with them.
txt.close()

print("Type the filename again: ", end=" ")
file_again = input("> ")

txt_again = open()

print(txt_again.read())

txt_again.close()