# Exercise 21: Functions Can Return Something

# Functions Can Return Something

# return to set variables to be a value from a function

# Our function is called with two arguments: a and b.
# We print out what our function is doing, in this case "ADDING."
# Then we tell Python to do something kind of backward: we return the addition of a + b.
# You might say this as, "I add a and b then return them."
# Python adds the two numbers. Then when the function ends,
# any line that runs it will be able to assign this a + b result to a variable.

# The return statement returns with a value from a function. 
# return without an expression argument returns None.
# Falling off the end of a function also returns None.


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Heigth: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

# Study Drills

weight2 = float(input("What's your weight? "))

number1 = divide(iq, 2)
number2 = multiply(weight2, number1)
number3 = subtract(height, number2)
number4 = add(age, number3)

print(f"The same result: {number4}")

# Write out a formula
# Try 24 + 34 / 100 - 1023
result1 = add(subtract(divide(34, 100), 1023), 24)
result2 = 24 + 34 / 100 - 1023
print(f"Are the results same?\nResult1: {result1}\nResult2: {result2}")


# Default Argument Values
# Specify a default value for one or more arguments.
# This creates a function that can be called with fewer arguments than it is defined to allow.

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# This function can be called in several ways:
# giving only the mandatory argument: ask_ok('Do you really want to quit?')
# giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# The default values are evaluated at the point of function definition in the defining scope, so that
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# will print 5

# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# This will print
# [1]
# [1, 2]
# [1, 2, 3]

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Keyword Arguments 
# kwarg = value
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# This function can be called in any of the following ways:
# In a function call, keyword arguments must follow positional arguments.
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# When a final formal parameter of the form **name is present, it receives a dictionary containing all keyword arguments except for those corresponding to a formal parameter.
# This may be combined with a formal parameter of the form *name which receives a tuple containing the positional arguments beyond the formal parameter list. (*name must occur before **name.)
# For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Special parameters
# / *
# Consider the following example function definitions paying close attention to the markers / and *:
def standard_arg(arg):
    print(arg)
standard_arg(2)
standard_arg(arg=2)

def pos_only_arg(arg, /):
    print(arg)
# The second function pos_only_arg is restricted to only use positional 
# parameters as there is a / in the function definition:
pos_only(1)

def kwd_only_arg(*, arg):
    print(arg)
# The third function kwd_only_args only allows keyword arguments as indicated 
# by a * in the function definition:
kwd_only_arg(arg=3)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

# Recap
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# • Use positional-only if you want the name of the parameters to not be available to the user.
# • Use keyword-only when names have meaning and the function definition is 
# more understandable by being explicit with names or you want to prevent 
# users relying on the position of the argument being passed.
# • For an API, use positional-only to prevent breaking API changes 
# if the parameter’s name is modified in the future.


# Arbitrary Argument Lists
# The least frequently used option is to specify that a function can be called with an arbitrary number of arguments.
# These arguments will be wrapped up in a tuple.

def concat(separator, *args):  # def concat(*args, separator="/"):
    return separator.join(args)


# Unpacking Argument Lists
# The reverse situation occurs when the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments
# For instance, the built-in range() function expects separate start and stop arguments.
# If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:
args = [3, 6]
list(range(*args))  # call with arguments unpacked from a list

# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# the Fibonacci series returns a list of the numberes instead of printing it
def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        # The statement result.append(a) calls a method of the list 
        # object result. A method is a function that ‘belongs’ to an object 
        # and is named obj.methodname, where obj is some 
        # object (this may be an expression), and methodname is the name of 
        # a method that is defined by the object’s type. 
        # Different types define different methods. Methods of different 
        # types may have the same name without causing ambiguity. 
        # It is possible to define your own object types and methods, using classes.

        #result += [a] # this is equivalent, but less efficient then append
        a, b = b, a + b
    return result

f100 = fib2(100) # call it
f100 # write the result
