# Tour of the Standard Library

# Operating System Interface (The os module)

# Be sure to use the import os style instead of from os import *. 
# This will keep os.open() from shadowing the built-in open() function which operates much differently.
import os
os.getcwd() # Return the current working directory
# 'D:\\Projects\\LPTHW'
os.system('mkdir today') # Run the command mkdir in the system shell
os.chdir('/Projects/LPTHW/today') # # Change current working directory

# The built-in dir() and help() functions are useful as interactive aids for working with large modules like os:
dir(os)
# <returns a list of all module functions>
help(os)
# <returns an extensive manual page created from the module's docstrings>

# For daily file and directory management tasks, 
# the shutil module provides a higher level interface that is easier to use:
import shutil
shutil.copyfile('ex16_test.txt', 'today.txt')
shutil.move('today.txt', 'today')
shutil.move('today', 'now')

# File Wildcards
# The glob module provides a function for making file lists from directory wildcard searches:
import glob
glob.glob('*.py')

# Command Line Arguments
# Common utility scripts often need to process command line arguments. 
# These arguments are stored in the sys module’s argv attribute as a list.
import sys
print(sys.argv)

# Error Output Redirection and Program Termination
# The sys module also has attributes for stdin, stdout, and stderr. 
# The latter is useful for emitting warnings and error messages 
# to make them visible even when stdout has been redirected:
sys.stderr.write('Warning, log file not found starting a new one\n')
# Warning, log file not found starting a new one

# The most direct way to terminate a script is to use sys.exit().

# String Pattern Matching
# The re module provides regular expression tools for advanced string processing.
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:
'tea for too'.replace('too', 'two')

# Mathematics

# The math module gives access to the underlying C library functions for floating point math:
import math

# The random module provides tools for making random selections
import random
random.choice(['apple','pear','banana'])
random.sample(range(100), 10) # sampling without replacement
random.random() # random float
random.randrange(6) # random integer chosen from range(6)

# The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5] 
statistics.mean(data)
statistics.median(data)
statistics.variance(data)

# Internet Access
# Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:
from urllib.request import urlopen
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8') # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line: # Look for Eastern Time
            print(line)

# Note that the second example needs a mailserver running on localhost.
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
    Beware the Ides of March.
""")
server.quit()

# Dates and Times
# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
# datetime.date(2018, 4, 17)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1979, 2, 27)
age = now - birthday
age.days

# Data Compression
# Common data archiving and compression formats are directly supported by modules
#  including: zlib, gzip, bz2, lzma, zipfile and tarfile.
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# Performance Measurement
# Some Python users develop a deep interest in knowing the relative performance 
# of different approaches to the same problem. 
# Python provides a measurement tool that answers those questions immediately.

from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2;').timeit()
# In contrast to timeit’s fine level of granularity, the profile and pstats modules 
# provide tools for identifying time critical sections in larger blocks of code.

# Quality Control
# One approach for developing high quality software is to write tests for each 
# function as it is developed and to run those tests frequently during the development process.

# The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings.
# Test construction is as simple as cutting-and-pasting a typical call along with its results into the docstring. 
def average(values):
    """Computes the arithmetic mean of a List of numbers.
    
    >>> print(average([20, 30, 100]))
    40.0
    """
    return sum(values)/len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

# The unittest module is not as effortless as the doctest module, 
# but it allows a more comprehensive set of tests to be maintained in a separate file:
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() # Calling from the command line invokes all tests

with urlopen('http://intranet.ph.koop.cz/node/8891') as response:
    message = 'Nový termín nebyl zveřejněn.'
    for line in response:
        line = line.decode('utf-8')
        if 'http://i-app.zam.koop.int/seminar/registrace_b.aspx?' in line and 'e46f9bab-9aac    5-a755-fdb9ac74aa42' not in line:
            message = 'Přihlásit se na jógu!'
            # print(line)
    print(message)
    