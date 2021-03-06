# Symbol Review

# Keywords
# https://www.programiz.com/python-programming/keyword-list#with

# and, or, not
if 5 > 2 and True:
    print("and")
if not False:
    print("not")
if True or False:
    print("or")

# as
# Now we can refer to the math module with this name.
# from - Importing specific parts of a module.
from sys import exit as cau
choice = input("Zadej Ahoj a ukončíš program. >>> ")
if choice == "Ahoj":
    print("as")
    cau(0)

# assert
# Is used for debugging purposes
# If the condition is true, nothing happens. But if the condition is false, 
# AssertionError is raised.
a = 4
assert a < 5, "The value is OK"
#assert a > 5, "The value of a is too small"

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

j = 0
while j < 10 :
    if j== 5:
        break

    print(j)
    j += 1

# class
# class is used to define a new user-defined class in Python.


# def
def jan_is_the_best():
    print("Jan is the best!")

jan_is_the_best()

# continue
# break and continue are used inside for and while loops to alter their normal behavior.
# continue causes to end the current iteration of the loop, but not the whole loop.
for i in range(0, 7):
    if i == 5:
        continue
    print(i)

# del
# del is used to delete the reference to an object
a = "Del is not used"
print(a)
# del a
# print(a)

# del is also used to delete items from a list or a dictionary
names = ["Jan", "Ondrej", "Filip", "Karel"]

for name in names:
    print(name)

del names[1]

for name in names:
    print(name)


# if, elif, else
def how_big(number):
    if number < 5:
        print("Less than five.")
    elif number < 10:
        print("Less then ten but more than five.")
    else:
        print("More than ten.")

how_big(2)
how_big(7)
how_big(11)

# except, raise, try
# send with exceptions in Python.

# Exceptions are basically errors that suggests something went wrong while executing our program.
# IOError, ValueError, ZeroDivisionError, ImportError, NameError, TypeError etc. are few examples of exception in Python.
# try...except blocks are used to catch exceptions in Python.


# We can raise an exception explicitly with the raise keyword
def reciprocal(num):
    try:
        r = 1/num
    except:
        print("Exception caught")
        return
    return r

    # finally is used with try…except block to close up resources or file streams.
    # Using finally ensures that the block of code inside it gets executed 
    # even if there is an unhandled exception
    # finally:
        # print("Finally, this is the end of the reciprocal function.")

print(reciprocal(10))
print(reciprocal(0))

# raise
# We could have also raised the ZeroDivisionError explicitly by checking the input
# and handled it elsewhere as follows:
def reciprocal1(num):
        if num == 0:
            raise ZeroDivisionError('cannot divide')
        r = 1/num
        return r

print(reciprocal1(10))
#print(reciprocal1(0))

#from
# print("Cosinus of 1 is", math.cos(1))

from math import cos
print("Cosinus of 1 is", cos(1))

# global
# global is used to declare that a variable inside the function is global (outside the function)
# If we need to modify the value of a global variable inside a function, then we must declare it with global.
# Otherwise a local variable with that name is created.

x = 6 # local variable

def example():
    global x
    z = 5
    print(z)
    print(x)
    # x += 100 # UnboundLocalError: local variable 'x' referenced before assignment
    x += 100
    print(x) 

    globx = x
    print(globx)
    globx += 5
    print(globx)
    return globx


globvar = 10
def read1():
    print(globvar)
def write1():
    global globvar
    globvar = 5
def write2():
    globvar = 15

read1()
write1()
read1()
write2()
read1()

# in
c = [1, 2, 3, 4]
print("2 in c", 2 in c)

for n in c:
    print(n)

# is
# is is used in Python for testing object identity. While the == operator is 
# used to test if two variables are equal or not, 
# is is used to test if the two variables refer to the same object
# Like == to test equality.
# It returns True if the objects are identical and False if not.
print("[] == []", [] == [])
print("[] is []", [] is [])
# An empty list or dictionary is equal to another empty one.
# But they are not identical objects as they are located separately in memory.
# This is because list and dictionary are mutable (value can be changed).

# lambda
# lambda is used to create an anonymous function (function with no name).
# It is an inline function that does not contain a return statement.
# It consists of an expression that is evaluated and returned.
# Lambda functions can be used wherever function objects are required. 
# They are syntactically restricted to a single expression. 
# Semantically, they are just syntactic sugar for a normal function definition.
a = lambda x: x*2
for i in range(1, 6):
    print(a(i))

s = lambda y: y**y
print(s(3))

def make_incrementator(n):
    return lambda x: x + n

f = make_incrementator(42)
f(0)
f(1)

# The above example uses a lambda expression to return a function. 
# Another use is to pass a small function as an argument:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs

# pass
# Suppose we have a function that is not implemented yet, but we want to implement it in the future.
# Simply writing,
# def function(args):
# in the middle of a program will give us IndentationError.
# Instead of this, we construct a blank body with the pass statement.
def function(args):
    pass

# return
def square(a):
    print("Calculate square a * a: ", a * a)
    return a * a

print(square(4))

# with
# https://www.programiz.com/python-programming/keyword-list#with
# with X as Y: pass

# yield
# yield is used inside a function like a return statement. But yield returns a generator
# Generator is an iterator that generates one item at a time.
# A large list of value will take up a lot of memory. Generators are useful in this situation
# as it generates only one value at a time instead of storing all the values in memory.
# Pause here and return to caller.
# For example,
g = (2**x for x in range(100))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# And so on… This type of generator is returned by the yield statement from a function.
# Here is an example.
def generator():
    for i in range(6):
        yield i*i

g = generator()
for i in g:
    print(i)
# Here, the function generator() returns a generator that generates square of numbers from 0 to 5.
# This is printed in the for loop.

# Generators are a simple and powerful tool for creating iterators. 
# They are written like regular functions but use the yield statement 
# whenever they want to return data. Each time next() is called on it, 
# the generator resumes where it left off (it remembers all the data values 
# and which statement was last executed). 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# What makes generators so compact is that 
# the __iter__() and __next__() methods are created automatically.
# Another key feature is that the local variables and execution state are automatically saved between calls. 
# When generators terminate, they automatically raise StopIteration. 
# In combination, these features make it easy to create iterators with no more effort than writing a regular function.

# Generator Expressions

# Some simple generators can be coded succinctly as expressions using a 
# syntax similar to list comprehensions but with parentheses instead of square brackets.
# Generator expressions are more compact but less versatile than full generator definitions 
# and tend to be more memory friendly than equivalent list comprehensions.
# Examples:
sum(i*i for i in range(4))
# 14

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))
# ['f', 'l', 'o', 'g']
