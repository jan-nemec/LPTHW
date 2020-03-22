# Exercise 2
# Print character and specifid index in string

input_string = input("Enter a string: ")

try:
    index = int(input("Enter an integer: "))
    print(input_string[index])
except ValueError:
    print("Invalid number")
except IndexError:
    print("Index is out of bounds")