# Else and If
# The keyword ‘elif’ is short for ‘else if’
# An if … elif … elif … sequence is a substitute for the switch or 
# case statements found in other languages.

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
elif trucks < people:
    print("Will be this printed?")
# What happens if multiple elif blocks are True?
# Python starts and the top runs the first block that is True, 
# so it will run only the first one.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# Study Drills
if cars > people and cars > trucks:
    print(f"The maximum is: {cars}")
elif people > trucks:
    print("The maximum is: {}".format(people))
else:
    print("The maximum is:", trucks)
