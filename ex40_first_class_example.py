# Classes
# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state. 
# Class instances can also have methods (defined by its class) for modifying its state

# When a class definition is entered, a new namespace is created, 
# nd used as the local scope — thus, all assignments to local variables go into this new namespace.
class Song(object):
    """docstring for Song"""

# In practice, the statements inside a class definition will usually be function definitions, 
# but other statements are allowed, and sometimes useful — we’ll come back to this later. 
    def __init__(self, lyrics): # The function definitions inside a class normally have a peculiar form of argument list, dictated by the calling conventions for methods
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    # Study Drill
    def choose_me_first_rhyme(self):
        print(self.lyrics[0])

    def choose_me_last_rhyme(self):
        print(self.lyrics[-1])

    def choosen_rhyme(self, number):
        print(self.lyrics[number])

# __doc__ is also a valid attribute, returning the docstring belonging to the class: "A simple example class".
Song.__doc__

# Class instantiation...Song()
happy_bday = Song(["Happy birthday to you.",
                   "I don't want to get sued!",
                   "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Scopes and Namespaces Example
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print('After local assignment:', spam)
    do_nonlocal()
    print('After nonlocal assignment:', spam)
    do_global()
    print('After global assignment:', spam)

scope_test()
print("In global scope:", spam)
# The output of the example code is:
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

# Note how the local assignment (which is default) didn’t change scope_test’s binding of spam. 
# The nonlocal assignment changed scope_test’s binding of spam, 
# and the global assignment changed the module-level binding
# You can also see that there was no previous binding for spam before the global assignment.

# Class and Instance Variables
# Generally speaking, 
# instance variables are for data unique to each instance and 
# class variables are for attributes and methods shared by all instances of the class:
class Pig:
    # tricks = [] # mistaken use of a class variable

    kind = 'canine' # class variable shared by all instances because just a single list would be shared by all Pig instances

    def __init__(self, name):
        self.name = name # instance variable unique to each instance
        self.tricks = [] # creates a new empty list for each pig
    
    def add_trick(self, trick):
        self.tricks.append(trick)

p = Pig('Piggy')
r = Pig('Buddy')

p.kind # shared by all pigs
r.kind # shared by all pigs
p.name # unique to p
r.name # unique to r

p.add_trick('roll over')
r.add_trick('play dead')

p.tricks # ['roll over']
r.tricks # ['play dead']

# Inheritance

# The syntax for a derived class definition looks like this:
#class DerivedClassName(BaseClassName):
#    <statement-1>

# when the base class is defined in another module:
# class DerivedClassName(modname.BaseClassName):

# There is a simple way to call the base class method directly: 
# just call BaseClassName.methodname(self, arguments). 

# Python has two built-in functions that work with inheritance:
# isinstance() #  to check an instance’s type
# issubclass() # to check class inheritance

# Multiple Inheritance
# class DerivedClassName(Base1, Base2, Base3):

# Private Variables
# “Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. 
# However, there is a convention that is followed by most Python code: 
# a name prefixed with an underscore (e.g. _spam) should be treated 
# as a non-public part of the API (whether it is a function, a method or a data member). 
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

# Odds and Ends
# Sometimes it is useful to have a data type similar to the Pascal “record” or C “struct”,
# bundling together a few named data items. An empty class definition will do nicely:
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000




skakal_pes = Song(["Skákal pes,", "přes oves,", "přes zelenou louku."])

skakal_pes.sing_me_a_song()

holka_modrooka_lyrics = ["Holka modrooka", "nesedavej u potoka.", "V potoce se voda točí,", "podemele tvoje oči."]
holka_modrooka = Song(holka_modrooka_lyrics)

holka_modrooka.sing_me_a_song()
holka_modrooka.choose_me_first_rhyme()
holka_modrooka.choose_me_last_rhyme()

print("Zadej rým, který chceš zobrazit?")
wanted_rhyme = int(input(">>> "))
holka_modrooka.choosen_rhyme(wanted_rhyme)
