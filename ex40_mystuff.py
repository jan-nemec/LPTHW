def apple():
	print("I AM APLLES!")


def fib(n):    # write Fibonacci series up to n
	a, b = 0, 1
	while b < n:
		print(b, end=' ')
		a, b = b, a + b
	print()

# this is just a variable
tangerine = "Living reflection of a dream"

# Executing modules as scripts
# When you run a Python module with
# python ex40_mystuff.py <arguments>
# the code in the module will be executed, just as if you imported it, 
# but with the __name__ set to "__main__". 
# That means that by adding this code at the end of your module:

if __name__ == "__main__":
	import sys
	fib(int(sys.argv[1]))
	print(__name__)

# you can make the file usable as a script as well as an importable module, 
# because the code that parses the command line only runs 
# if the module is executed as the "main" file:

# python ex40_mystuff.py 50

# If the module is imported, the code is not run:
# import ex40_mystuff

# This is often used either to provide a convenient user interface to a module,
# or for testing purposes (running the module as a script executes a test suite).

# The Module Search Path
# When a module named spam is imported, the interpreter first searches for a built-in module with that name. 
# If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.
# 	The directory containing the input script (or the current directory when no file is specified).
#	PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
#	The installation-dependent default

# "Compiled" Python files

# To speed up loading modules, Python caches the compiled version of each module 
# in the __pycache__ directory under the name module.version.pyc, 
# where the version encodes the format of the compiled file; 
# it generally contains the Python version number. 
# For example, in CPython release 3.3 the compiled version of spam.py would be cached as __pycache__/spam.cpython-33.pyc. 
# This naming convention allows compiled modules from different releases and different versions of Python to coexist.
# Python checks the modification date of the source against the compiled version to see 
# if it’s out of date and needs to be recompiled. This is a completely automatic process.

# A program doesn’t run any faster when it is read from a .pyc file than when it is read from a .py file; 
# the only thing that’s faster about .pyc files is the speed with which they are loaded.