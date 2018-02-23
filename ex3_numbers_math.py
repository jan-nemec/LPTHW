# Exercise 3: Numbers and Math
"""Numbers and Math"""

print("I will count my chickens:")

print("Hens", 25.0 + 30.0 / 6.0)
print("Roosters", 180.0 - 25.0 * 3.0 % 4.0)

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