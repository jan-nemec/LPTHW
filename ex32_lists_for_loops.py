# Loops and Lists

# Lists are exactly what their name says: a container of things that are organized in order from first to last.

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Lists also support operations like concatenation:
squares = [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]
# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes[3] = 64

# You can also add new items at the end of the list, by using the append() method
cubes.append(216)
cubes.append(7 ** 3)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Assignment to slices is also possible
letters[2:5] = ['C', 'D', 'E']

# clear the list by replacing all the elements with an empty list
letters[:] = []

# The built-in function len() also applies to lists
len(letters)

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x[0]
x[0][1]

# this first kind of for-loop goes throug a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# also possible
elements1 = list(range(0, 6))

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")

for i in elements1:
    print(f"Element1 was: {i}")
