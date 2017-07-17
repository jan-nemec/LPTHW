# While Loops

 # What they do is simply do a test like an if-statement, but instead of running the code block once, they jump back to the "top" where the while is, and repeat.
 # A while-loop runs until the expression is False.
 # Here's the problem with while-loops: Sometimes they do not stop.

# To avoid these problems, there are some rules to follow:
# 1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
# 2. Review your while statements and make sure that the boolean test will become False at some point.
# 3. When in doubt, print out your test variable at the top, (in the middle) and bottom of the while-loop to see what it's doing.

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
