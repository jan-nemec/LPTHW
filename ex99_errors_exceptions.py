# Errors and Exceptions
# There are (at least) two distinguishable kinds of errors: 
# syntax errors 
#   and 
# exceptions (run-time errors).

# Syntax Errors

# Syntax errors, also known as parsing errors
# You write some code that isn't allowed in the Python language.
# The parser repeats the offending line and displays a little ‘arrow’ pointing 
# at the earliest point in the line where the error was detected. 
# The error is caused by (or at least detected at) the token preceding the arrow.

# Exceptions (run-time errors)

# Even if a statement or expression is syntactically correct, 
# it may cause an error when an attempt is made to execute it. 
# Errors detected during execution are called exceptions.

# Run-time errors - they only occur at the time that program is run.
# While trying to execute the program Python raised an error. Whenever an
# error occurs, Python stops executing the program and displays the error in
# IDLE's interactive window. The text that gets displayed for an error is called
# a traceback.

# ZeroDivisionError: division by zero
# NameError: name 'spam' is not defined
# Can't convert 'int' object to str implicitly

# Exceptions come in different types, and the type is printed as part of the message:
# the types in the example are ZeroDivisionError, NameError and TypeError. 

# Handling Exceptions

# It is possible to write programs that handle selected exceptions.
while True:
    try:
        x = int(input('Please enter a number:'))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

# 1. The try clause (the statement(s) between the try and except keywords) is executed.
# 2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# 3. If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
#    Then if its type matches the exception named after the except keyword, the except clause is executed, 
#    and then execution continues after the try statement.
#    The first matching except clause is triggered.
# 4. If an exception occurs which does not match the exception named in the except clause, 
#    it is passed on to outer try statements; 
#    if no handler is found, it is an unhandled exception and execution stops with a message.

# A try statement may have more than one except clause, to specify handlers for different exceptions. 
# An except clause may name multiple exceptions as a parenthesized tuple, for example:

# except (RuntimeError, TypeError, NameError):

# A class in an except clause is compatible with an exception if it is the same class or a base class thereof.

# The last except clause may omit the exception name(s), to serve as a wildcard.
# Use this with extreme caution, since it is easy to mask a real programming error in this way!
# It can also be used to print an error message and then re-raise the exception (allowing a caller to handle the exception as well):

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err: # When an exception occurs, it may have an associated value, also known as the exception’s argument.
    # If an exception has arguments, they are printed as the last part (‘detail’) of the message for unhandled exceptions.
    print("OS error: {0}".format(err))
    print("The exception instance: ", type(err))
    print("Arguments stored in args: ", err.args)
    print(err) # the exception instance defines __str__() so the arguments can be printed directly without having refernce .args
    # x = err.args # unpack args
    # print('x =', x)
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

# The try … except statement has an optional else clause, which, when present, 
# must follow all except clauses. 
# It is useful for code that must be executed if the try clause does not raise an exception.

# else:
#    f.close()

# Exception handlers don’t just handle exceptions if they occur immediately in the try clause, 
# but also if they occur inside functions that are called (even indirectly) in the try clause
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# Raising Exceptions

# The raise statement allows the programmer to force a specified exception to occur.
raise NameError('HiThere')

# The sole argument to raise indicates the exception to be raised. 
# This must be either an exception instance or an exception class # (a class that derives from Exception).

# If you need to determine whether an exception was raised but don’t intend to handle it, 
# a simpler form of the raise statement allows you to re-raise the exception:
try:
    raise NameError('Hi There')
except NameError:
    print('An Exception catched!')
    raise

# User-defined Exceptions

# Programs may name their own exceptions by creating a new exception class
# Exceptions should typically be derived from the Exception class
# When creating a module that can raise several distinct errors, 
# a common practice is to create a base class for exceptions defined by that module, 
# and subclass that to create specific exception classes for different error conditions:
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input
    
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.
    
    Attributes:
        previous -- state at the beginning of the transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """
    
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# Defining Clean-up Actions

# The try statement has another optional clause which is intended to define 
# clean-up actions that must be executed under all circumstances.
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# A more complicated example:
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

# divide("10", 2)
# The TypeError raised by dividing two strings is not handled by the except clause 
# and therefore re-raised after the finally clause has been executed.

# In real world applications, the finally clause is useful for releasing external resources 
# (such as files or network connections), regardless of whether the use of the resource was successful.

# Predefined Clean-up Actions

# Some objects define standard clean-up actions to be undertaken when the object is no longer needed, 
# regardless of whether or not the operation using the object succeeded or failed. 
for line in open('ex16_test.txt'):
    print(line)
# The problem with this code is that it leaves the file open 
# for an indeterminate amount of time after this part of the code has finished executing. 

# The with statement allows objects like files to be used in a way 
# that ensures they are always cleaned up promptly and correctly.
with open('ex16_test.txt') as f:
    for line in f:
        print(line, end="")
# After the statement is executed, the file f is always closed, 
# even if a problem was encountered while processing the lines. 
# Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.
