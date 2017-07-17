# Exercise 21: Functions Can Return Something

# Functions Can Return Something

# return to set variables to be a value from a function

# Our function is called with two arguments: a and b.
# We print out what our function is doing, in this case "ADDING."
# Then we tell Python to do something kind of backward: we return the addition of a + b. 
# You might say this as, "I add a and b then return them."
# Python adds the two numbers. Then when the function ends, 
# any line that runs it will be able to assign this a + b result to a variable.
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
print(f"Are the results same?\nResult1: {result1}\nResult2: {result2}" )