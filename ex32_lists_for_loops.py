# Loops and Lists

# Before you can use a for-loop, you need a way to store the results of loops 
# somewhere. The best way to do this is with lists. 

# Lists are exactly what their name says: a container of things 
# that are organized in order from first to last. Lists cen be written as
# a list of comma-separated values (items) between square brackets.

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Lists also support operations like concatenation:
squares = [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]

# Like strings (and all other bult-in sequence types), lists can be indexed
# and sliced:
squares[0]
squares[-3:] # slicing returns a new list

cubes = [1, 8, 27, 65, 125]
# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes[3] = 64

# You can also add new items at the end of the list, by using the append() method
# The statement cubes.append(a) calls a method of the list object result.
# A method is a function that ‘belongs’ to an object and is named obj.methodname, where obj is some object (this may be an expression),
# and methodname is the name of a method that is defined by the object’s type.
# Different types define different methods.
# Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using classes)
# The method append() shown in the example is defined for list objects; it adds a new element at the end of the list.
# In this example it is equivalent to cubes = cubes + [216], but more efficient.
cubes.append(216)
cubes.append(7 ** 3)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Assignment to slices is also possible
letters[2:5] = ['C', 'D', 'E'] # replace some values
# now remove them
letters[2:5] = []
# clear the list by replacing all the elements with an empty list
letters[:] = []

# A shallow copy of the list:
squares2 = squares[:]

# The built-in function len() also applies to lists
len(letters)

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x[0]
x[0][1]

# To iterate over the indices of a sequence, you can 
# combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# In many ways the object returned by range() behaves as if it is a list, 
# but in fact it isn’t. It is an object which returns the successive items 
# of the desired sequence when you iterate over it, but it doesn’t really 
# make the list, thus saving space.
# We say such an object is iterable, that is, suitable as a target for 
# functions and constructs that expect something from which they can 
# obtain successive items until the supply is exhausted. 
# We have seen that the for statement is such a construct, 
# while an example of function that takes an iterable is sum()
sum(range(4))  # 0 + 1 + 2 + 3
# Maybe you are curious about how to get a list from a range. 
# Here is the solution:
list(range(4))


# for Statements
# Python’s for statement iterates over the items of any sequence 
# (a list or a string), in the order that they appear in the sequence.
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# this first kind of for-loop goes throug a list
for number in the_count:
    print(f"This is count {number}")

# an initial sub-sequence of the Fibonacci series
# the sum of two elements defines the next
a, b = 0, 1 # a multiple assignment
while a < 10:
    print(a)
    a, b = b, a+b
    # the expressions on the right-hand side are all evaluated first before 
    # any of the assignments take place
    # The right-hand side expressions are evaluated from the left to the right.



# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# Python’s for statement iterates over the items of any sequence (a list or a string),
# in the order that they appear in the sequence.

# we can also build lists, first start with an empty one
elements = []


# The range() function
# If you do need to iterate over a sequence of numbers, 
# the built-in function range() comes in handy.
for i in range(5):
    print(i)

range(5, 10)
# 5, 6, 7, 8, 9

range(0, 10, 3)
# 0, 3, 6, 9

range(-10, -100, -30)
# -10, -40, -70   

# then use the range function to do 0 to 5 counts
# It is possible to let the range start at another number,
# or to specify a different increment (even negative; sometimes this is called the ‘step’):
for i in range(6):  # for i in range(len(a)):
    # for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# also possible
elements1 = list(range(0, 6))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

for i in elements1:
    print(f"Element1 was: {i}")

# Code that modifies a collection while iterating over that same collection 
# can be tricky to get right. Instead, it is usually more straight-forward 
# to loop over a copy of the collection or to create a new collection:
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# If you need to modify the sequence you are iterating over while inside 
# the loop (for example to duplicate selected items),
# it is recommended that you first make a copy.
# Iterating over a sequence does not implicitly make a copy.
# The slice notation makes this especially convenient:
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

# The function list() creates lists from iterables:
# list(range(5))
# output: [0, 1, 2, 3, 4]

# break and continue Statements:
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            # else clause is not executed when the loop is terminated by a break statement.
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

# The continue statement continues with the next iteration of the loop:
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# pass Statements:
# The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
# For example:
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

# This is commonly used for creating minimal classes:

# Another place pass can be used is as a place-holder for a function or conditional body when you are working on new code, allowing you to keep thinking at a more abstract level.


class MyEmptyClass:
    pass


def initlog(*args):
    pass   # Remember to implement this!
