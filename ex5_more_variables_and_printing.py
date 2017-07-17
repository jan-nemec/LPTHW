# Exercise 5: More Variables and Printing
"""More Variables and Printing"""

my_name = 'Jan Nemec'
my_age = 38  # not a lie
my_height = 180  # cm
my_weight = 88  # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

inch = 0.393700787
pound = 2.20462262
my_height2 = my_height * inch
my_weight2 = round(my_weight * pound)

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall. It's {round(my_height2, 2)} inches.")
print(f"He's {my_weight} kg heavy. It's {my_weight2} pounds.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_weight + my_height
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
