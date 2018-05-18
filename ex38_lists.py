# Doing Things to Lists

# When you write
#   mystuff.append('hello')
# you are actually setting off a chain of events inside Python to cause something to happen to the mystuff list. Here's how it works:

# 1. Python sees you mentioned mystuff and looks up that variable. It might have to look backward to see if you created it with =, if it is a function argument, or if it's a global variable. Either way it has to find the mystuff first.
# 2. Once it finds mystuff it reads the . (period) operator and starts to look at variables that are a part of mystuff. Since mystuff is a list, it knows that mystuff has a bunch of functions.
# 3. It then hits append and compares the name to all the names that mystuff says it owns. If append is in there (it is), then Python grabs that to use.
# 4. Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.
# 5. That extra argument is ... mystuff! I know, weird, right? But that's how Python works, so it's best to just remember it and assume that's the result. What happens, at the end of all this, is a function call that looks like: append(mystuff, 'hello') instead of what you read, which is mystuff.append('hello').

#class Thing(object):
#    def test(message): #def test(self, message):
#        print(message)

#a = Thing()
#a.test("hello")

# error: TypeError: test() takes 1 positional argument but 2 were given
# For now you see how Python said test() takes exactly 1 argument (2 given).
# If you see this, it means that Python changed a.test("hello") to test(a, "hello")
# and that somewhere someone messed up and didn't add the argument for a.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one)  # append(stuff, next_one) Call append on stuff with argument next_one
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:6]))  # super stellar!

# lists
# They are simply ordered lists of facts you want to store and access randomly or linearly by an index.

# You use a list whenever you have something that matches the list data structure's useful features:

# If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
# If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
# If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.

# Study Drills
fruits_vegetables = ['Banana', 'Apple', 'Orange', 'Carrot']

more_fruits_vegetables = ["Cucumber", "Plumb", "Peach", "Onion", "Garlic", "Lemon", "Garbage"]
while len(fruits_vegetables) < 10:
    next_item = more_fruits_vegetables.pop()
    print("Adding fruit or vegetable:", next_item)
    fruits_vegetables.append(next_item)
    print(f"Count: {len(fruits_vegetables)}")

print(', '.join(fruits_vegetables))


# Rewrite using for loop
# ex32 - We can also build lists, first start with an empty one
girls = ["Naďa", "Petra", "Michaela"]
next_girls = ["Karla", "Lucie", "Eliška", "Tereza", "Olga", "Veronika", "Irena", "Monika", "Štěpánka"]
print("Number of girls:", len(girls))

for i in range(0, 10 - len(girls)):
    next_girl = next_girls[i]
    print("Adding next girl:", next_girl)
    girls.append(next_girl)
    print(f"Count: {len(girls)}")

print("*".join(girls))

# The for statement calls iter() on the container object. 
# The function returns an iterator object that defines the method __next__() 
# which accesses elements in the container one at a time. 
# When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate
s = 'abc'
it = iter(s)

next(it)
# a
next(it)
# b
next(it)
# c
# next(it)
# Traceback (most recent call last):



# More on Lists
# Here are all of the methods of list objects:

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

# list.insert(i, x)
# Insert an item at a given position. 
# The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, 
# and a.insert(len(a), x) is equivalent to a.append(x).

# list.remove(x)
# Remove the first item from the list whose value is x. It is an error if there is no such item.

# list.pop([i])
# Remove the item at the given position in the list, and return it. 
# If no index is specified, a.pop() removes and returns the last item in the list. 
# (The square brackets around the i in the method signature denote that the parameter is optional,
# not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

# list.clear()
# Remove all items from the list. Equivalent to del a[:].

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
# The optional arguments start and end are interpreted as in the slice notation 
# and are used to limit the search to a particular subsequence of the list. 
# The returned index is computed relative to the beginning of the full sequence rather than the start argument.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].

# You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 
# This is a design principle for all mutable data structures in Python.

# Using Lists as Stacks
# The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). 
# To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop().

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack.pop()
stack.pop()
stack

# Using Lists as Queues
# It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”); 
# however, lists are not efficient for this purpose. 
# While appends and pops from the end of list are fast, 
# doing inserts or pops from the beginning of a list is slow 
# (because all of the other elements have to be shifted by one).

# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends. 
# For example:
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
# 'Eric'
queue.popleft()                 # The second to arrive now leaves
# 'John'
queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])

# List Comprehensions
# List comprehensions provide a concise way to create lists. 
# Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, 
# or to create a subsequence of those elements that satisfy a certain condition.
squares = []
for x in range(10):
    squares.append(x**2)

# Note that this creates (or overwrites) a variable named x that still exists after the loop completes. 
# We can calculate the list of squares without any side effects using:
squares2 = list(map(lambda x: x**2, range(10)))
# or
squares3 = [x**2 for x in range(10)] # which is more concise and readable.
# A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

# For example, this listcomp combines the elements of two lists if they are not equal:
[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# and it’s equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
combs

# If the expression is a tuple (e.g. the (x, y) in the previous example), it must be parenthesized.
[(x, x**2) for x in range(6)]

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# Nested List Comprehensions
# Consider the following example
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]  
    [9, 10, 11, 12]
]

# The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)] # the nested listcomp is evaluated in the context of the for that follows it
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# this example is equivalent to:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
transposed

# In the real world, you should prefer built-in functions to complex flow statements. 
# The zip() function would do a great job for this use case:
list(zip(*matrix))

# The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
del a[2:4]
del a[:] # clear the entire list (which we did earlier by assignment of an empty list to the slice a = [])

# del can also be used to delete entire variables:
a = 88
del a

# Tuples and Sequences

# Though tuples may seem similar to lists, they are often used in different situations and for different purposes. 
# Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking (see later in this section) 
# or indexing (or even by attribute in the case of namedtuples). 
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list

# A tuple consists of a number of values separated by commas>>> t = 12345, 54321, 'hello!'
t = 12345, 54321, 'hello!'
t[0]
# 12345
t
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# Tuples are immutable:
t[0] = 88888
# TypeError: 'tuple' object does not support item assignment
# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# ([1, 2, 3], [3, 2, 1])

# This is called, appropriately enough, sequence unpacking and works for any sequence on the right-hand side. 
# Sequence unpacking requires that there x, y, z = tare as many variables on the left side of the equals sign as there are elements in the sequence.


# A special problem is the construction of tuples containing 0 or 1 items: 
# the syntax has some extra quirks to accommodate these. 
# Empty tuples are constructed by an empty pair of parentheses; 
# a tuple with one item is constructed by following a value with a comma 
# (it is not sufficient to enclose a single value in parentheses). Ugly, but effective. 
empty = ()
singleton = 'hello',

# Sets
# Python also includes a data type for sets. 
# A set is an unordered collection with no duplicate elements. 
# Basic uses include membership testing and eliminating duplicate entries. 
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# {'orange', 'banana', 'pear', 'apple'}
'orange' in basket # fast membership testing
# True

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}

# Similarly to list comprehensions, set comprehensions are also supported:
a = {x for x in 'abracadabra' if x not in 'abc'}