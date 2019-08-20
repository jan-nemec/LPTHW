# Understanding Python slices
# https://blog.lerner.co.il/understanding-python-slices/

# you have a Python string, and want to grab a substring from it. 
# The best way to do so is with a “slice”
s = 'abcdefghij'
print(s[3:8])

# Slices work on all sequences in Python. 
mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
mylist[3:7]

# While “for” loops in Python don’t explicitly use numeric indexes, slices do.
# For example, if I’m interested in iterating over letters 3-7 
# in my string “s” from above, I won’t (and can’t) use a C-like “for” loop, 
# starting the loop at index 3 and ending at index 7.
for one_letter in s[3:7]:
    print(one_letter)

# Remember that a slice from type X will always return a new object of type X. 
# Thus, slicing a string returns a string, 
# while slicing a list returns a list and 
# slicing a tuple returns a tuple.

# Slice syntax is more flexible than this: 
# You can leave off the starting index, ending index, or both.
s
s[:5]
s[5:]
s[5:-1] # not the same as s[5:] -- doesn't include the end

# Because slices create new objects, 
# you can sometimes use them to avoid problems with mutable data:
mylist = [10, 20, 30]
biglist = [mylist, mylist]
mylist[0] = '!'
biglist
# [['!', 20, 30], ['!', 20, 30]]
# In the above code, changing “mylist” affected “biglist”, 
# because both names were still pointing (one directly, one indirectly) 
# to the original list. 
# By contrast, if I use slices, I can avoid this:
mylist = [10, 20, 30]
biglist = [mylist[:], mylist[:]] # put copies, no mylist
mylist[0] = '!'
biglist
# [[10, 20, 30], [10, 20, 30]]

# !: Note that this isn’t a perfect solution; if you’re copying complex data 
# structures, then you’ll probably want to look at the “copy” module, 
# and explore its “copy” and “deepcopy” methods.

# By default, a slice uses each element from the sequence 
# on which it’s working. But what if we only want every other element?
# Then we can use the (optional) third part of slice syntax.
mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
mylist[2:7]
# [30, 40, 50, 60, 70]
mylist[2:7:2]
# [30, 50, 70]
import string
s = string.ascii_lowercase
s[5:20]
s[5:20:3]
s[:25:4] # from start, until (not including) 25, step size 4
s[2::4] # from 2, through the end, step size 4

# It gets even better when you discover that the step size can be negative, 
# which allows us to retrieve values in reverse order 
# from the original data structure. Just remember, 
# in such cases, that the start needs to be bigger than the end:
s[20:5:-1] # from 20 to 5 (not including), step size 1
s[:5:-4] # from 20 to 5 (not including), step size 4
s[20::-2] # from 20 to the beginning, step size 2
s[::-1] # no indexes? from end to start, backwards
s[5:20:-5] # Start is smaller, and negative step?  Bad news...

# You can use variables in a slice:
s = 'abcdefghij'
i = 3
j = 7
s[i]
s[i:j]
s[::i]

# Normally, if you try to retrieve from an index that’s beyond the bounds of 
# the data structure, you’ll get an error:
s[15]
# But slices are far more forgiving; if you go off of the edge of a slice, 
# then Python will simply stop at the edge of your sequence:
s[:15]

# You can also assign to slices. For the most part, 
# this means modifying multiple elements in a list:
mylist = [10, 20, 30, 40, 50, 60, 70]
mylist[3:5]
mylist[3:5] = 'XY'
mylist
# You can expand and contract a list by assigning more items:
mylist[3:5] = 'WXYZ'
mylist
# We can similarly shrink it:
mylist[3:7] = [99, 98]
mylist

# While we normally think about only sequences as being sliceable, 
# other objects can potentially work with slices, too. 
# For example, the “range” object in Python 3 is sliceable
r = range(100, 300, 3)
r[4:8]
r[10:20:3]

# Python provides a “slice” builtin that I’ve never used, 
# but which I can imagine would be useful 
# if you want to reuse a slice multiple times:
s = 'abcdefghij'
myslice = slice(2, 8, 2)
s[myslice]

myslice = slice(None, None, -2)
s[myslice]

# What if you want your own objects to be sliceable? 
# Truth be told, there’s not much to do:
# The __getitem__ method is used for retrieving individual items 
# as well as slices; while there used to be a __getslice__ method, 
# nowadays you are expected to write __getitem__ such that it handles 
# individual indexes and slices. In many cases, that’s trivially easy to do:
class Foo():
    def __init__(self, x):
        self.x = x
    def __getitem__(self, index):
        return self.x[index]

f = Foo('abcdefghij')
f[3]
f[3:5]