# Exercise 19: Functions and Variables

# Functions and Variables

# This shows all the different ways we're able to give our function cheese_and_crackers the values it needs to print them.
# We can give it straight numbers. We can give it variables.
# We can give it math. We can even combine math and variables.

# Is it bad to have global variables (like amount_of_cheese) with the same name as function variables?
# Yes, since then you're not quite sure which one you're talking about.
# But sometimes necessity means you have to use the same name,
# or you might do it on accident. Just avoid it whenever you can.

# Use CamelCase for classes and lower_case_with_underscores for functions and methods. 

# Function Style
# * For various reasons, programmers call functions that are part of
#	classes "methods"
# * Instead of naming your functions after what the function does, instead
#	name it as if it's a command. Same as pop is saying "Hey list, pop this
# 	off." It isn!t called remove_from_end_of_list because even though that's
#	what it does, that's not command to a list.
# * Keep your functions small and simple.

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 20
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def tennis_costs(hours_played):
	cost_of_hour = 670
	total_costs = hours_played * cost_of_hour
	print(f"Total costs: {total_costs}")

print("Study Drill:")
hours_of_tennis = int(input("How many hours of tennis did you play this month: "))
tennis_costs(hours_of_tennis)