# Exercise 3: Numbers and Math
"""Numbers and Math"""

print("I will count my chickens:")

print("Hens", 25.0 + 30.0 / 6.0)
print("Roosters", 180.0 - 25.0 * 3.0 % 4.0) # 177 (* First Then %)
# What is the order of operations?
# In the United States we use an acronym called PEMDAS which stands for
# Parentheses Exponents Multiplication Division Addition Subtraction. 
# The mistake people make with PEMDAS is to think this is a strict order,
# as in "Do P, then E, then M, then D, then A, then S." 
# The actual order is you do the multiplication and division (M&D) in one step,
# from left to right, then you do the addition and subtraction in one step 
# from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).

print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", -2 < 5)
print("Is it greater or equal?", -2 <= 5)
print("Is it less or equal?", -2 >= 5)

# There is full support for floating point; operators with mixed type operands 
# convert the integer operand to floating point:
4 * 3.75 - 1
# 14.0

# In interactive mode, the last printed expression is assigned to the variable _.
# This means that when you are using Python as a desk calculator,
# it is somewhat easier to continue calculations, for example:
tax = 12.5 / 100
price = 100.50
price * tax
price + _
# 113.0625
round(_, 2)
# 113.06

print('4 ** 3 =', 4 ** 3)

17 // 3  # floor division discards the fractional part
# // Integer Division - The // operator ﬁrst divides the number on the left by 
# the number on the right and then rounds down to an integer.
# This might not give the value you expect when one of the numbers is negative.
# For example, -3 // 2 returns -2. First, -3 is divided by 2 to get -1.5.
# Then -1.5 is rounded down to -2. On the other hand, 3 // 2 returns 1

# 5
17 % 3  # the % operator returns the remainder of the division
# 2

5 ** 2 # 5 squared
# 25

-3**2 
# will be interpreted as -(3**2) and thus result in -9. 
# To avoid this and get 9, you can use 
(-3)**2

1000000.0
1_000_000.0
1e6 
type(1e6)  # <class 'float'>
# Unlike integers, floats do have a maximum size. The maximum
# floating-point number depends on your system, but something like
# 2e400 ought to be well beyond most machines’ capabilities.

-1 + (-3*2 + 4)
# The *, /, //, and % operators all have equal precedence, or priority,
# in an expression, and each of these has a higher precedence than the +
# and - operators. This is why 2*3 - 1 returns 5 and not 4. 2*3 is evaluated
# ﬁrst, because * has higher precedence than the - operator.
# PEP8: If operators with diﬀerent priorities are used, consider
# adding whitespace around the operators with the low-#est priority(ies). 
# Use your own judgment; however, never use more than one space, and always 
# have the same amount of whitespace on both sides of a binary operator.

# Make Python Lie to You
0.1 + 0.2
# 0.30000000000000004
# No, it isn’t a bug! It’s a сoating-point representation error, and
# it has nothing to do with Python. It’s related to the way floating-point
# numbers are stored in a computer’s memory.

# The number 0.1 can be represented as the fraction 1/10. Both the
# number 0.1 and it’s fraction 1/10 are decimal representations,
# or base 10 representations. Computers, however, store floating-
# point numbers in base 2 representation, more commonly called
# binary representation.

# When represented in binary, something familiar yet possibly unex-
# pected happens to the decimal number 0.1. The fraction 1/3 has no
# ﬁnite decimal representation. That is, 1/3 = 0.3333... with inﬁnitely
# many 3’s after the decimal point. The same thing happens to the frac-
# tion 1/10 in binary.

# The binary representation of 1/10 is the following inﬁnitely repeating
# fraction:
# 0.00011001100110011001100110011...

# Math Functions and Number Methods

# round() - rounding numbers to some number of decimal places
# Python 3 rounds numbers according to a strategy called rounding
# ties to even. A tie is any number whose last digit is 5. 2.5 and 3.1415
# are ties, but 1.37 is not.
round(2.5)
# 2
round(3.5)
# 4

# Rounding ties to even is the rounding strategy recommended
# for floating-point numbers by the IEEE (Institute of Electrical
# and Electronics Engineers) because it helps limit the impact
# rounding has on operations involving lots of numbers.

# You can round a number to a given number of decimal places:
round(3.14159, 3)
# 3.142

# abs() - getting the absolute value of a number
abs(5)
# 5
abs(-3.0)
# -3.0

# pow() - raising a number to some power
# ** operator
# the pow() function. pow() takes two arguments. The ﬁrst is the base, 
# that is the number to be raised to a power, and the second argument 
# is the exponent.
pow(2 ,3)
# 8

pow(2, -2)

# What’s the diﬀerence between ** and pow()? The pow() function
# accepts an optional third argument that computes the ﬁrst number
# raised to the power of the second number and then takes the modulo
# with respect to the third number.
# pow(x, y, z) is equivalent to (x ** y) % z
pow(2, 3, 2)
# First, 2 is raised to the power 3 to get 8. Then 8 % 2 is calculated, which
# is 0 because 2 divides 8 with no remainder

# Check if a Float Is Integral
num = 2.5
num.is_integer()
# False

num = 2.0
num.is_integer()
# True

# Complex Numbers
# A complex number is a number with two dis-tinct components: a real component 
# and an imaginary component
# a common method is to indicate the real component with the letter i and 
# the imaginary component with the letter j. For example, 1i +2j is the complex
#number with real part 1 and imaginary part 2.
 n = 1 + 2j
 n
 # (1+2j)
 n.real # property - don't perform any action, just return some information
 # about the number.
 # 1.0
 n.imag
# 2.0
n.conjugate() - # method - performs an action on the complex number
# For any complex number, its conjugate is the complex number with
# the same real part and an imaginary part that is the same in absolute
# value but with the opposite sign. 
# (1-2j)
