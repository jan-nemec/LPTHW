# Modules Are Like Dictionaries

mystuff = {"apple": "I AM APPLES!"}
print(mystuff)

# Modules
# 1. A Python file with some functions or variables in it ..
# 2. You import that file.
# 3. And you can access the functions or variables in that module with the . (dot) operator.

import ex40_mystuff as my_stuff

my_stuff.apple()
print(my_stuff.tangerine)

# Refer back to the dictionary,
# and you should start to see how this is similar to using a dictionary,
# but the syntax is different.
print(mystuff['apple'])  # get apple from dict
my_stuff.apple()  # get apple from the module
print(my_stuff.tangerine)  # get thing, it's just a variable

# Classes Are Like Modules

# Class - a blueprint for building a copy of that type of thing
# You can think about a module as a specialized dictionary that can store Python code so you can access it with the . operator.
# Python also has another construct that serves a similar purpose called a class.
# A class is a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator.

# Here's why classes are used instead of modules:
# You can take this MyStuff class and use it to craft many of them, millions at a time if you want, and each one won't interfere with each other.
# When you import a module there is only one for the entire program unless you do some monster hacks.

class MyStuff(object):
    """docstring for MyStuff"""

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APLLES!")

# That concept is called "instantiate", which is just a fancy, obnoxious, overly smart way to say "create."
# "Instantiate" just means to create an object from the class
# When you instantiate a class what you get is called an object

# The first line is the "instantiate" operation
# 1. Python looks for MyStuff() and sees that it is a class you've defined.
# 2. Python crafts an empty object with all the functions you've specified in the class using def.
# 3. Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
# 4. In the MyStuff function __init__ I then get this extra variable self, which is that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
# 5. In this case, I set self.tangerine to a song lyric and then I've initialized this object.
# 6. Now Python can take this newly minted object and assign it to the thing variable for me to work with.
# The resulting created mini-module is called an object, and you then assign it to a variable to work with it.

# Why do I need self when I make __init__ or other functions for classes?
# With self.cheese = 'Frank' it's very clear you mean the instance attribute self.cheese

thing = MyStuff()
thing.apple()
print(thing.tangerine)