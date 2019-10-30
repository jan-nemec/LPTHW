# Virtual Environments and Packages

# A virtual environment is a semi-isolated Python environment that allows 
# packages to be installed for use by a particular application, 
# rather than being installed system wide.

# Deprecated since version 3.6: 
# pyvenv was the recommended tool for creating virtual environments 
# for Python 3.3 and 3.4, and is deprecated in Python 3.6.

# If application A needs version 1.0 of a particular module but application B 
# needs version 2.0, then the requirements are in conflict and installing 
# either version 1.0 or 2.0 will leave one application unable to run.

# The solution for this problem is to create a virtual environment, 
# a self-contained directory tree that contains a Python installation 
# for a particular version of Python, plus a number of additional packages.

# Creating Virtual Environments

# venv module
# venv will usually install the most recent version of Python 
# that you have available. If you have multiple versions of Python on your 
# system, you can select a specific Python version 
# by running python3 or whichever version you want.

# python3 -m venv tutorial-env

# This will create the tutorial-env directory if it doesn’t exist, 
# and also create directories inside it containing a copy of the 
# Python interpreter, the standard library, and various supporting files.

# python -m venv venv

# Activation

# Windows
# venv\Scripts\activate

# Unix
#source venv/bin/activate

# Activating the virtual environment will change your shell’s prompt
#  to show what virtual environment you’re using.

# Managing Packages with pip

# You can install, upgrade, and remove packages using a program called pip.
# By default pip will install packages from the Python Package Index, 
# <https://pypi.python.org/pypi>. 
# You can browse the Python Package Index by going to it in your web browser, 
# or you can use pip’s limited search feature:

# pip search astronomy

# You can install the latest version of a package by specifying a package’s name:

# pip install ipython

#You can also install a specific version of a package by 
# giving the package name followed by == and the version number:

# pip install requests==2.6.0

# It’s also possible to specify an exact or minimum version directly on the command line.
# When using comparator operators such as >, < or some other special character 
# which get interpreted by shell, the package name and the version should be enclosed within double quotes:

# python -m pip install SomePackage==1.0.4    # specific version
# python -m pip install "SomePackage>=1.0.4"  # minimum version

# You can supply a different version number to get that version, or you can run
# pip install --upgrade to upgrade the package to the latest version:

# Passing the --user option to python -m pip install will install a package 
# just for the current user, rather than for all users of the system.

# pip install --upgrade requests

# pip uninstall followed by one or more package names will remove the packages 
# from the virtual environment.

# pip uninstall ipython flask

# pip show will display information about a particular package:

# pip show ipython

# pip list will display all of the packages installed in the virtual environment:

# pip list

# pip freeze will produce a similar list of the installed packages, 
# but the output uses the format that pip install expects. 
# A common convention is to put this list in a requirements.txt file:

# pip freeze > requirements.txt

# The requirements.txt can then be committed to version control and shipped 
# as part of an application. 
# Users can then install all the necessary packages with install -r:

# pip install -r requirements.txt


# Creating the Skeleton Project Directory

# mkdir projects
# cd projects/
# mkdir skeleton
# cd skeleton
# mkdir bin NAME tests docs

# bin directory - Why do we need a bin/ folder? This is just a standard place
# to put scripts that are run on the command line, not a place to put modules.

# https://docs.python.org/3/distutils/setupscript.html

# Using the Skeleton
# Whenever you want to start a new project, just do this:
# 1. Make a copy of your skeleton directory and name it after new project.
# 2. Rename the NAME directory to be the name of your project or whatever
# you want to call your root module.
# 3. Edit your setup.py to have all the information for your project.
# 4. Rename tests/NAME_tests.py to also have your module name.
# 5. Check it's all working by using nosetests.
# 6. Start coding.
