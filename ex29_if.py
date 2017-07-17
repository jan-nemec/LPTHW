# What If

people = 20
cats = 30
dogs = 15

if people < cats:
# Why does the code under the if need to be indented four spaces?
# A colon at the end of a line is how you tell Python you are going to create a new "block" of code,
# and then indenting four spaces tells Python what lines of code are in that block.
# This is exactly the same thing you did when you made functions in the first half of the book.

# Python expects you to indent something after you end a line with a : (colon).
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if not(people < dogs):
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

if people != dogs:
    print("People aren't dogs.")

dogs += 5  # -=

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

if people != dogs:
    print("People aren't dogs.")

if True:
    print("This is true.")