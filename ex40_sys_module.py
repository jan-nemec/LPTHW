# Standard Modules
# Python comes with a library of standard modules, 
# described in a separate document, the Python Library Reference (“Library Reference” hereafter).

# One particular module deserves some attention: sys, which is built into every Python interpreter.
import sys
sys.ps1
# '>>> '
sys.ps2
# '... '

# sys.path
# The variable sys.path is a list of strings that determines the interpreter’s search path for modules. 
# It is initialized to a default path taken from the environment variable PYTHONPATH, 
# or from a built-in default if PYTHONPATH is not set. You can modify it using standard list operations:
sys.path.append('/ufs/guido/lib/python')

# The dir() Function
# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings:
# Note that it lists all types of names: variables, modules, functions, etc.
import sys, ex40_mystuff
dir(ex40_mystuff)
dir(sys)

# Without arguments, dir() lists the names you have defined currently:
a = [1, 2, 3, 4, 5]
dir()

# dir() does not list the names of built-in functions and variables. 
# If you want a list of those, they are defined in the standard module builtins:
import builtins
dir(builtins)

# Packages
# Packages are a way of structuring Python’s module namespace by using “dotted module names”. 
# For example, the module name A.B designates a submodule named B in a package named A.

#sound/                          Top-level package
#      __init__.py               Initialize the sound package
#      formats/                  Subpackage for file format conversions
#              __init__.py
#              wavread.py

# The __init__.py files are required to make Python treat the directories as containing packages.
# In the simplest case, __init__.py can just be an empty file, 
# but it can also execute initialization code for the package or set the __all__ variable.

# Users of the package can import individual modules from the package, for example:
# import sound.effects.echo

# This loads the submodule sound.effects.echo. It must be referenced with its full name.
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# An alternative way of importing the submodule is:
# from sound.effects import echo

# This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows:
# echo.echofilter(input, output, delay=0.7, atten=4)

# Yet another variation is to import the desired function or variable directly:
# from sound.effects.echo import echofilter

# Again, this loads the submodule echo, but this makes its function echofilter() directly available:
# echofilter(input, output, delay=0.7, atten=4)


# Importing * From a Package

# Now what happens when the user writes from sound.effects import *?
# The only solution is for the package author to provide an explicit index of the package. 
# The import statement uses the following convention: 
# if a package’s __init__.py code defines a list named __all__, 
# it is taken to be the list of module names that should be imported when from package import * is encountered
# Although certain modules are designed to export only names that follow certain patterns when you use import *, 
# it is still considered bad practice in production code.


# Intra-package References

# When packages are structured into subpackages (as with the sound package in the example), 
# you can use absolute imports to refer to submodules of siblings packages. 
# For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, 
# it can use from sound.effects import echo

# You can also write relative imports, with the from module import name form of import statement. 
# From the surround module for example, you might use:
# from . import echo
# from .. import formats
# from ..filters import equalizer