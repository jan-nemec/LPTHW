# Inheritance Versus Composition

# Most of the uses of inheritance can be simplified or replaced with
# composition, and multiple inheritance shoud be avoided at all costs.

# What is inheritance?
# Inheritance is used to indicate that one class will get most or all of
# its features from a parent class. This happens implicitly whenever you
# write class Foo(Bar), which says "Make a class Foo that inherits from Bar."
# Doing this lets you put common functionality in the Bar class, then
# specialize that functionality in the Foo class as needed.

# There are three ways that the parent and child class can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.

# 1. Implicit Inheritance


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")


class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# Even though I'm calling son.implicit() and even though Child does not have an
# implicit function defined, it still work, and it calls the one defined in
# Parent.

# 2. Override Explicitly
# The problem with having fucntions called implicitly is sometimes you want
# the child to behave differently. In this case you want to override the 
# function in the child, effectively replacing the functionallity.
# To do this just define a function with the same name in Child.


class Parent(object):

    def override(self):
        print("PARENT override()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# 3. Alter Before or After
# A special case of overriding where you want to alter the behaviour before
# or after the Parent class's version runs. You first override the function
# just like in the last example, but then you use a Python built-in function
# named super to get the Parent version to call.


class Parent(object):

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# All Three Combined


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

# The Reason for super()
# We get int trouble with a thing called multiple inheritance. Multiple
# inheritance is when you define a class that inherits from one or more
# classes, like this:
class SuperFun(Child, BadStuff):
    pass
# This is like saying, "Make a class named SuperFun that inherits from the
# classes Child and BadStuff at the same time."

# In this case, whenever you have implicit actions on any SuperFun instance,
# Python has to look-up the possible function in the class hierarchy for
# both Childe and BadStuff, but it needs to do this in a consistent order. To
# do this Python uses "method resolution order" (MRO) and an algorithm called
# C3 to get it straight.
# Python gives you super() function, which handles all of this for you.

# Using super() with __init__
# The most common use of super() is actually in __init__ funcion base classes.
# This is usually the only place where you need to do some things in a child,
# then complete the initialization in the parrent.

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

# This is pretty much the same as Child.altered example above, except I'm
# setting some variables in the __init__ before having the Parent initialize
# with its Parent __init__.

# Composition
# Another way to do the exact same thing is just to use other classes modules.
# Two of the three inheritances involve writing new code to replace or alter
# functionality. This can be replicated by just calling functions in a module.

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        self.other.altered()
        print("CHILD, AFTER PARENT altered()") 

son = Child()
son.implicit()
son.override()
son.altered()

# There is not a parent-child is-a relationship.
# This is a has-a relationship, where Child has-a Other.
# I could ask myself if I need this Other to be a class, and could I just
# make it into a module named other.py?

# When to Use Inheritance or Composition
# We want reusable code:
# Inheritance solves this by creating a mechanism for you to have implied
# features in base classes.
# Composition solves this by giving you modules and the capability to call 
# functions in other classes.

# My three guidelines for when to do which:
# 1. Avoid multiple inheritance at all costs, as it's too complex to be
# reialble.
# 2. Use composition to package code into modules that are used in many
# different unrelated places and situations.
# 3. Use Inheritance only when there are clearly related reusable pieces
# of code that fit under a single common concept or if you have
# to because of something you're using.

# Do not be a slave of these rules!

