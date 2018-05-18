# Brief Tour of the Standard Library - Part II

# More advanced modules that support professional programming needs
# These modules rarely occur in small scripts

# Output Formatting

# The reprlib module provides a version of repr() cusomized for abbreviated
# displays of large or deeply nested containers:
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))

# The pprint module offers more sophisticated control over printing in a way
# that is readable by the interpreter. When the result is longer than one line,
# the "pretty printer" adds line breaks and indentation to more clearly reveal
# data structure:
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(t)
pprint.pprint(t, width=30)

# The textwrap module formats paragraphs of text to fit a given screen width
import textwrap
doc = """The wrap() method is just like fill() except that it returs
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

# The locale accesses a database of culture specific data formats
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv() # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)

locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True)

# Templating
# The string module includes versatile Template class
# The format uses placeholder names formed by $ with valid Python identifiers
# Surrounding the placeholder with braces allows it to be followed by more
# alphanumeric letters with no intervenening spaces. Writing $$ creates a
# single escaped $:
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
# The substitute() method raises a KeyError when a placeholder is not supplied

# The safe_substitute() method may be more appropriate for mail-merge style
# applications, user supplied data may be incomplete - it will leave placeholders
# unchanged if data is missing:
t = Template('Return the $item to $owner')
d = dict(item='unladen swallow')
t.substitute(d)
t.safe_substitute(d)

# Template subclasses can specify a custom delimiter.
# For example, a batch renaming utility for a photo browser may elect to use percent
# signs for placeholders such as the current date, image sequence number, file format:
import time, os.path
from string import Template
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1080.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# Another application for templating is separating program logic from the details of multiple output formats. 
# This makes it possible to substitute custom templates for XML files, plain text reports, and HTML web reports.

# Working with Binary Data Record Layouts

# The struct module provides pack() and unpack() functions for working with variable length binary record formats.
# The following example shows how to loop through header information in a ZIP file without using the zipfile module. 
# Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. 
# The "<" indicates that they are standard size and in little-endian byte order:
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

# Multi-threading

# Threading is a technique for decoupling tasks which are not sequentially dependent. 
# Threads can be used to improve the responsiveness of applications 
# that accept user input while other tasks run in the background. 

# The following code shows how the high level threading module 
# can run tasks in background while the main program continues to run:
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

# While those tools are powerful, minor design errors can result in problems that are difficult to reproduce. 
# So, the preferred approach to task coordination is to concentrate all access to a resource in a single thread 
# and then use the queue module to feed that thread with requests from other threads. 
# Applications using Queue objects for inter-thread communication 
# and coordination are easier to design, more readable, and more reliable.

# Logging

# The logging module offers a full featured and flexible logging system. 
# At its simplest, log messages are sent to a file or to sys.stderr:

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning: config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error --- shutting down')

# By default, informational and debugging messages are suppressed and the output is sent to standard error. 

# Weak References

# Python does automatic memory management (reference counting for most objects 
# and garbage collection to eliminate cycles). 
# The memory is freed shortly after the last reference to it has been eliminated.

# This approach works fine for most applications but occasionally there is 
# a need to track objects only as long as they are being used by something else. 
# Unfortunately, just tracking them creates a reference that makes them permanent. 
# The weakref module provides tools for tracking objects without creating a reference. 
# When the object is no longer needed, it is automatically removed from a weakref table and a callback is triggered for weakref objects. 
# Typical applications include caching objects that are expensive to create:

import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive
# 10
del a                       # remove the one reference
gc.collect()                # run garbage collection right away
# 0
d['primary']                # entry was automatically removed

# Tools for Working with Lists

# Many data structure needs can be met with the built-in list type. 
# However, sometimes there is a need for alternative implementations with different performance trade-offs.

# array - The array module provides an array() object that is like a list 
# that stores only homogeneous data and stores it more compactly. 
# The following example shows an array of numbers stored as two byte unsigned binary numbers (typecode "H") 
# rather than the usual 16 bytes per entry for regular lists of Python int objects:
from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
array('H', [10, 700])

# deque - The collections module provides a deque() object that is like a list 
# with faster appends and pops from the left side but slower lookups in the middle. 
# These objects are well suited for implementing queues and breadth first tree searches:
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

# bisect - In addition to alternative list implementations, 
# the library also offers other tools such as the bisect module with functions for manipulating sorted lists:
import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))

# heapq - The heapq module provides functions for implementing heaps based on regular lists. 
# The lowest valued entry is always kept at position zero. 
# This is useful for applications which repeatedly access the smallest element but do not want to run a full list sort:
from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries

# Decimal Floating Point Arithmetic

# The decimal module offers a Decimal datatype for decimal floating point arithmetic. 
# Compared to the built-in float implementation of binary floating point, the class is especially helpful for:
    # * financial applications and other uses which require exact decimal representation,
    # * control over precision,
    # * control over rounding to meet legal or regulatory requirements,
    # * tracking of significant decimal places, or
    # * applications where the user expects the results to match calculations done by hand.
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
# Decimal('0.74')
round(.70 * 1.05, 2)
# 0.73

# Exact representation enables the Decimal class to perform modulo calculations
#  and equality tests that are unsuitable for binary floating point:
Decimal('1.00') % Decimal('.10')
# Decimal('0.00')
1.00 % 0.10
# 0.09999999999999995

sum([Decimal('0.1')]*10) == Decimal('1.0')
# True
sum([0.1]*10) == 1.0
# False

Decimal.from_float(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')

# Another helpful tool is the math.fsum() function which helps mitigate loss-of-precision during summation.
math.fsum([0.1] * 10) == 1.0

# The decimal module provides arithmetic with as much precision as needed:
getcontext().prec = 36
Decimal(1) / Decimal(7)
# Decimal('0.142857142857142857142857142857142857')
1/7
# 0.14285714285714285

# fractions
# Another form of exact arithmetic is supported by the fractions module which 
# implements arithmetic based on rational numbers (so the numbers like 1/3 can be represented exactly).
from fractions import Fraction
Fraction.from_float(0.1)
# Fraction(3602879701896397, 36028797018963968)

# Python provides tools that may help on those rare occasions when you really 
# do want to know the exact value of a float. 
# The float.as_integer_ratio() method expresses the value of a float as a fraction:
x = 3.14159
x.as_integer_ratio()
# Since the ratio is exact, it can be used to losslessly recreate the original value:
x == 3537115888337719/1125899906842624
# True

# The float.hex() method expresses a float in hexadecimal (base 16), 
# again giving the exact value stored by your computer:
x.hex()
# '0x1.921f9f01b866ep+1'
x == float.fromhex('0x1.921f9f01b866ep+1')
# True