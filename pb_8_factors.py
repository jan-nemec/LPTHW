# 8.4 - Challenge: Find the Factors of a Number
# Prints out the factors of the number


num = int(input('Enter a positive integer: '))

divisor = 1
while divisor <= num:
    if num % divisor == 0:
        print(f"{divisor} is a factor of {num}")
    divisor += 1
