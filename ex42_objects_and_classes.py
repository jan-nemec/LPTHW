# Is-A, Has-A, Objects, and Classes

# An important concept that you have to understand is the difference between a class and an object.
# The problem is, there is no real "difference" between a class and an object.
# They are actually the same thing at different points in time.

# What is the difference between a fish and a salmon?

# A salmon is a kind of fish, so I mean it's not different.
# But at the same time, a salmon is a particular type of fish so it's actually different from all other fish.
# That's what makes it a salmon and not a halibut.

# You know a salmon is a kind of fish and that there are other kinds of fish.

# Let's take it one step further. Let's say you have a bucket full of three salmon and because you are a nice person,
# you have decided to name them Frank, Joe, and Mary. Now, think about this question:

# What is the difference between Mary and a salmon?

# You know that Mary is a salmon, so she's not really different. She's just a specific "instance" of a salmon.
# Joe and Frank are also instances of salmon. What do I mean when I say instance?
# I mean they were created from some other salmon and now represent a real thing that has salmon-like attributes.

# Now for the mind-bending idea: Fish is a class, and Salmon is a class, and Mary is an object.
# There you have it: Mary is a kind of salmon that is a kind of fish---object is a class is a class.

# I will show you two tricks to help you figure out whether something is a class or an object.

# is-a
# A phrase to say that something inherits from another,
# as in a "salmon" is-a "fish."

# has-a
# A phrase to say that something is composed of other things or has a trait,
# as in "a salmon has-a mouth."


## Animal is-a object
class Animal(object):

    def __init__(self, sound):
        self.sound = sound

        self.number_of_legs = None

    def welcome(self):
        print("Welcome to the nature!")

## ?? | Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ?? | Dog has-a name
        self.name = name
        # 3. Python then looks to see if you made a "magic" __init__ function, and if you have it calls that function to initialize your newly created empty object.
        # 4. In the MyStuff function __init__ I then get this extra variable self, which is that empty object Python made for me, and I can set variables on it just like you would with a module, dictionary, or other object.
        # 5. In this case, I set self.tangerine to a song lyric and then I've initialized this object.


## ?? | Person is-a object
class Person(object):

    def __init__(self, name):
        ## ?? | Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
        # That makes sure that the self.pet attribute of that class is set to a default of None.

## ?? | Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        # That's how you can run the __init__ method of a parent class reliably.
        # Note that the syntax changed in Python 3.0: you can just say super().__init__()
        # instead of super(ChildB, self).__init__() which IMO is quite a bit nicer.

        ## ?? | Employee has-a salary
        self.salary = salary

## ?? | Fish is-a object
class Fish(object):
    pass

## ?? | Salmon is-a Fish
class Salmon(Fish):
    pass

## ?? | Halibut is-a Fish
class Halibut(Fish):
    pass

## Cat is-a Animal
class Cat(Animal):
    def __init__(self, sound, name):
        super(Cat, self).__init__(sound)

        self.name = name

## rover is-a Dog
rover = Dog("Rover")

## ?? | satan is-a Cat
satan = Cat("Miau", "Satan")

## ?? | mary is-a Person
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ?? | flipper is-a Fish
flipper = Fish()

## ?? | crouse is-a Fish
crouse = Salmon()

## ?? | harry is-a Fish
harry = Halibut()

# About class Name(object)
# class is-a object" comes in.
# They decided that they would use the word "object," lowercased,
# to be the "class" that you inherit from to make a class. Confusing, right?
# A class inherits from the class named object to make a class but it's not an object really it's a class,
# but do not forget to inherit from object.

# assume that Python always requires (object) when you make a class

# New-style classes inherit from object, or from another new-style class.
class NewStyleClass(object):
    pass

class AnotherNewStyleClass(NewStyleClass):  # if a new-style class inherits from another new-style class, then by extension, it inherits from object
    pass

# Old-style classes don't.

class OldStyleClass():
    pass

# Python 3.x:
# class MyClass(object): = new-style class
# class MyClass: = new-style class (implicitly inherits from object)

# When defining base classes in Python 3.x, you’re allowed to drop the object from the definition.
# However, this can open the door for a seriously hard to track problem…

# "Multiple inheritance"
# avoid it if you can

# Study Drills
print("-" * 25)
print(f"The dog name is {rover.name}.")
rover.welcome()
print(mary.pet.name, satan.name)
rover.number_of_legs = 4
print(f"Rover has {rover.number_of_legs} legs.")
print(satan.name, satan.sound)
print(frank.name, frank.salary)
