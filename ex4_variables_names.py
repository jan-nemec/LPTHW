# Exercise 4: Variables And Names
"""Variables And Names"""

cars = 100
space_in_a_car = 4.0
space_in_a_car2 = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
carpool_capacity2 = cars_driven * space_in_a_car2
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print(f"There are {cars} cars available.")
print("There are {0} cars available.".format(cars))
print("There are {} cars available.".format(cars))

print("There are only", drivers, "drivers available.")
print("There will be", cars_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We can transport", carpool_capacity2, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# The first line contains a multiple assignment: the variables a and b
# simultaneously get the new values 0 and 1. On the last line this is used again
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
