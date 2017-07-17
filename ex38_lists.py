# Doing Things to Lists

# When you write
#   mystuff.append('hello')
# you are actually setting off a chain of events inside Python to cause something to happen to the mystuff list. Here's how it works:

# 1. Python sees you mentioned mystuff and looks up that variable. It might have to look backward to see if you created it with =, if it is a function argument, or if it's a global variable. Either way it has to find the mystuff first.
# 2. Once it finds mystuff it reads the . (period) operator and starts to look at variables that are a part of mystuff. Since mystuff is a list, it knows that mystuff has a bunch of functions.
# 3. It then hits append and compares the name to all the names that mystuff says it owns. If append is in there (it is), then Python grabs that to use.
# 4. Next Python sees the ( (parenthesis) and realizes, "Oh hey, this should be a function." At this point it calls (runs, executes) the function just like normally, but instead it calls the function with an extra argument.
# 5. That extra argument is ... mystuff! I know, weird, right? But that's how Python works, so it's best to just remember it and assume that's the result. What happens, at the end of all this, is a function call that looks like: append(mystuff, 'hello') instead of what you read, which is mystuff.append('hello').

#class Thing(object):
#    def test(message): #def test(self, message):
#        print(message)

#a = Thing()
#a.test("hello")

# error: TypeError: test() takes 1 positional argument but 2 were given
# For now you see how Python said test() takes exactly 1 argument (2 given).
# If you see this, it means that Python changed a.test("hello") to test(a, "hello")
# and that somewhere someone messed up and didn't add the argument for a.

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one)  # append(stuff, next_one) Call append on stuff with argument next_one
    print(f"There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:6]))  # super stellar!

# lists
# They are simply ordered lists of facts you want to store and access randomly or linearly by an index.

# You use a list whenever you have something that matches the list data structure's useful features:

# If you need to maintain order. Remember, this is listed order, not sorted order. Lists do not sort for you.
# If you need to access the contents randomly by a number. Remember, this is using cardinal numbers starting at 0.
# If you need to go through the contents linearly (first to last). Remember, that's what for-loops are for.

# Study Drills
fruits_vegetables = ['Banana', 'Apple', 'Orange', 'Carrot']

more_fruits_vegetables = ["Cucumber", "Plumb", "Peach", "Onion", "Garlic", "Lemon", "Garbage"]
while len(fruits_vegetables) < 10:
    next_item = more_fruits_vegetables.pop()
    print("Adding fruit or vegetable:", next_item)
    fruits_vegetables.append(next_item)
    print(f"Count: {len(fruits_vegetables)}")

print(', '.join(fruits_vegetables))


# Rewrite using for loop
# ex32 - We can also build lists, first start with an empty one
girls = ["Naďa", "Petra", "Michaela"]
next_girls = ["Karla", "Lucie", "Eliška", "Tereza", "Olga", "Veronika", "Irena", "Monika", "Štěpánka"]
print("Number of girls:", len(girls))

for i in range(0, 10 - len(girls)):
    next_girl = next_girls[i]
    print("Adding next girl:", next_girl)
    girls.append(next_girl)
    print(f"Count: {len(girls)}")

print("*".join(girls))