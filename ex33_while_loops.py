# While Loops (indefinite iteration)

# Iteration means executing the same block of code over and over, 
# potentially many times. A programming structure that implements iteration 
# is called a loop.
    # In programming, there are two types of iteration, indefinite and definite:
    # With indefinite iteration, the number of times the loop is executed isn’t 
    # specified explicitly in advance. Rather, the designated block is executed 
    # repeatedly as long as some condition is met.

    # With definite iteration, the number of times the designated block will 
    # be executed is specified explicitly at the time the loop starts.

 # What they do is simply do a test like an if-statement, but instead of running the code block once, they jump back to the "top" where the while is, and repeat.
 # A while-loop runs until the expression is False.
 # Here's the problem with while-loops: Sometimes they do not stop.

# Python provides two keywords that terminate a loop iteration prematurely:
    # break
        # immediately terminates a loop entirely. 
        # Program execution proceeds to the first statement following the loop body.
    # continue
         # immediately terminates the current loop iteration. 
         # Execution jumps to the top of the loop, 
         # and the controlling expression is re-evaluated to determine 
         # whether the loop will execute again or terminate.

# To avoid these problems, there are some rules to follow:
# 1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
# 2. Review your while statements and make sure that the boolean test will become False at some point.
# 3. When in doubt, print out your test variable at the top, (in the middle) and bottom of the while-loop to see what it's doing.

#while <expr>:
#    <statement(s)>
# <statement(s)> represents the block to be repeatedly executed, 
# often referred to as the body of the loop. This is denoted with indentation,
# just as in an if statement.

# The controlling expression, <expr>, typically involves one or more variables
# that are initialized prior to starting the loop and then modified somewhere
# in the loop body.

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")

print(numbers)

for num in numbers:
    print(num)

print(f"i is: {i}")


# Study Drills
def fill_list(iterates, increment_by):
    """Fill the list"""
    j = 0
    numbers.clear()

    while j < iterates:
        print(f"At the top i is {j}")
        numbers.append(j)

        j += increment_by
        print("Numbers now:", numbers)
        print(f"At the bottom i is {j}")

fill_list(8, 2)

for num in numbers:
    print(num)

elements = []

for i in range(0, 10):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print("The Element is:", i)

# https://realpython.com/python-while-loop/
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

# The else Clause
# Python allows an optional else clause at the end of a while loop. 
# This is a unique feature of Python, not found in most other programming languages. 

#while <expr>:
#    <statement(s)>
#else:
#    <additional_statement(s)>

# About now, you may be thinking, “How is that useful?” 
# You could accomplish the same thing by putting those statements immediately 
# after the while loop, without the else:

#while <expr>:
    #<statement(s)>
#<additional_statement(s)>

# What’s the difference?
# When <additional_statement(s)> are placed in an else clause, 
# they will be executed only if the loop terminates “by exhaustion”—
# that is, if the loop iterates until the controlling condition becomes false.
# If the loop is exited by a break statement, the else clause won’t be executed.
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break;
    else:
        print('Loop done')
# This loop is terminated prematurely with break, so the else clause isn’t executed.
# The creator of Python, has actually said that, 
# if he had it to do over again, he’d leave the while loop’s else clause out of the language.

# When might an else clause on a while loop be useful? 
# One common situation is if you are searching a list for a specific item. 
# You can use break to exit the loop if the item is found, 
# and the else clause can contain code that is meant to be executed 
# if the item isn’t found:
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'
i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for the item not found
    print(s, 'not found in the list.')

# The code shown above is useful to illustrate the concept, 
# but you’d actually be very unlikely to search a list that way.

# First of all, lists are usually processed with definite iteration, not a while loop. 
# Secondly, Python provides built-in ways to search for an item in a list. 
# You can use the in operator:
if s in a:
    print(s, 'found in list.')
else:
    print(s, 'not found in list')

# The list.index() method would also work. 
# This method raises a ValueError exception if the item isn’t found 
# in the list, so you need to understand exception handling to use it. 
# In Python, you use a try statement to handle an exception.
try:
    print(a.index('corge'))
except ValueError:
    print(s, 'not found in list')

# Infinite Loops
# Remember that loops can be broken out of with the break statement. 
# It may be more straightforward to terminate a loop based on conditions 
# recognized within the loop body, rather than on a condition evaluated at the top.

a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))

# You can also specify multiple break statements in a loop:
#while True:
#    if <expr1>:  # One condition for loop termination
#        break
#    if <expr2>:  # Another termination condition
#        break
#    if <expr3>:  # Yet another
#        break

# In cases like this, where there are multiple reasons to end the loop, 
# it is often cleaner to break out from several different locations, 
# rather than try to specify all the termination conditions in the loop header.

# Nested while Loops
# a while loop can be contained within another while loop, as shown here:
a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))
    
# A break or continue statement found within nested loops applies to the 
# nearest enclosing loop:
#while <expr1>:
#    statement
#    statement
#
#    while <expr2>:
#        statement
#        statement
#        break  # Applies to while <expr2>: loop
#
#    break  # Applies to while <expr1>: loop

# Additionally, while loops can be nested inside if/elif/else statements, 
# and vice versa:
# if <expr>:
#     statement
#     while <expr>:
#         statement
#         statement
# else:
#     while <expr>:
#         statement
#         statement
#     statement

# while <expr>:
#     if <expr>:
#         statement
#     elif <expr>:
#         statement
#     else:
#         statement

#     if <expr>:
#         statement

# (One-Line while Loops)
# Remember that PEP 8 discourages multiple statements on one line. 
# If there are multiple statements in the block that makes up the loop body, 
# they can be separated by semicolons (;):
n = 5
while n > 0: n -= 1; print(n)

# as with an if statement
if True: print('foo')


# infinite loop
#answer = 0
#while True:
#    print('doing stuff')
