# Dictionaries, Oh Lovely Dictionaries

# A Dictionary (or "dict") is a way to store data just like a list,
# but instead of using only numbers to get the data, you can use almost anything.
# It is best to think of a dictionary as an unordered set of key: value pairs, 
# with the requirement that the keys are unique (within one dictionary.

# A dictionary is used to map or associate things you want to store to keys you need to get them.
# A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type.

# What would I use a dictionary for?
# When you have to take one value and "look up" another value. In fact, you could call dictionaries "look up tables."

# What if I need a dictionary, but I need it to be in order?
# Take a look at the collections.OrderedDict data structure in Python. Search for it online to find the documentation.

# Let's say you want to find out what the word "Honorificabilitudinitatibus" means.
# Today you would simply copy-paste that word into a search engine and then find out the answer,
# and we could say a search engine is like a really huge super complex version of the Oxford English Dictionary (OED).
# Before search engines what you would do is this:

# 1. Go to your library and get "the dictionary". Let's say it's the OED.
# 2. You know "honorificabilitudinitatibus" starts with the letter 'H' so you look on the side of the book for the little tab that has 'H' on it.
# 3. Then you'd skim the pages until you are close to where "hon" started.
# 4. Then you'd skim a few more pages until you found "honorificabilitudinitatibus" or hit the beginning of the "hp" words and realize this word isn't in the OED.
# 5. Once you found the entry, you'd read the definition to figure out what it means.
# This process is nearly exactly the way a dict works, and you are basically "mapping" the word "honorificabilitudinitatibus" to its definition.

# Performing list(d.keys()) on a dictionary returns a list of all the keys used in the dictionary, 
# in arbitrary order (if you want it sorted, just use sorted(d.keys()) instead). 
# To check whether a single key is in the dictionary, use the in keyword.

# Lists
# You can only use numbers to get items out of a list.

# What would I use a list for?
# Use a list for any sequence of things that need to be in order, and you only need to look them up by a numeric index.

things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

# Dicts
# a dict associates one thing to another, no matter what it is.
stuff = {'name': 'Jan', 'age': 38, 'height': 6 * 30 + 1.7}
stuff1 = dict([('name','Jan'),('age', 38)])
# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
stuff2 = dict(name='Jan', age=38)

print(stuff['name'])

print(stuff['height'])

stuff['city'] = "SF"
print(stuff['city'])

list(stuff.keys())
sorted(stuff.keys())
del stuff['city']
'city' in stuff

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}

# You will see that instead of just numbers
# we're using strings to say what we want from the stuff dictionary.
# We can also put new things into the dictionary with strings.
# It doesn't have to be strings though. We can also do this:

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])

print(stuff)

# delete items from the dictionary
del stuff['city']
del stuff[1]
del stuff[2]

print(stuff)

# A Dictionary Example
# "mapping" or "associating" is the key concept in a dictionary

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print("-" * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

# Looping Techniques

# When looping through dictionaries, the key and corresponding value 
# can be retrieved at the same time using the items() method.

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# When looping through a sequence, the position index and corresponding value 
# can be retrieved at the same time using the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, 
# the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in sorted order, 
# use the sorted() function which returns a new sorted list 
# while leaving the source unaltered.
sample = [0, 8, 55, 2, -1]
for num in sorted(sample):
    print(num)

# To loop over a sequence in reverse, 
# first specify the sequence in a forward direction 
# and then call the reversed() function.
for i in reversed(range(1, 10, 2)):
    print(i)

# It is sometimes tempting to change a list while you are looping over it; 
# however, it is often simpler and safer to create a new list instead.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

filtered_data

# Conditions
# in and  not in - check whether a value occurs (does not occur) in a sequence. 
# is and is not compare whether two objects are really the same object; this only matters for mutable objects like lists.
# Comparisons can be chained. For example, a < b == c
# Comparisons may be combined using the Boolean operators and and or, 
# and the outcome of a comparison (or of any other Boolean expression) may be negated with not.
# It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null
# 'Trondheim'

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
# state = states['Texas'] # KeyError: 'Texas'
state_safely = states.get('Texas')

print("State Texas:", state)
print("Safely state Texas:", state_safely)

#if not state:
#	print("Sorry, no Texas.")

if not state_safely:
    print("Safely sorry, no Texas.")

# get a city with a defalut value
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")

# Study Drills
kraje = {
    "Jižní Morava": "JM",
    "Jižní Čechy": "JČ",
    "Střední Čechy": "StČ",
    "Severní Čechy": "SČ",
    "Severní Morava": "SM",
    "Východní Čechy": "VČ",
    "Západní Čechy": "ZČ"
}

mesta = {
    "JM": "Brno",
    "JČ": "České Budějovice",
    "StČ": "Mladá Boleslav",
    "SČ": "Ústní nad Labem",
    "SM": "Ostrava",
    "VČ": "Pardubice",
    "ZČ": "Plzeň"
}

print(kraje)
print("." * 25)
print(f"Jižní Morava má zkratku: {kraje['Jižní Morava']}")
print("Krajské město na Jižní Moravě je:", mesta[kraje['Jižní Morava']])

praha = kraje.get('Praha')
print(praha)
if not praha:
    print("Omlouvám se, ale kraj Praha neexistuje.")

kraj = kraje.get("Praha", "Neexistuje")
print("Kraj Praha:", kraj)

for kraj, zkratka in list(kraje.items()):
    print(f"Kraj: {kraj} - {zkratka} Město: {mesta[zkratka]}")

import collections

# What if I need a dictionary, but I need it to be in order?
# Take a look at the collections.OrderedDict data structure in Python. Search for it online to find the documentation.
print('Regular dictionary:')
d = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E"
}

#d = {}
#d['c'] = 'C'
#d['b'] = 'B'
#d['e'] = 'E'
#d['d'] = 'D'
#d['a'] = 'A'

for k, v in d.items():  # k - key | v - value
    print(k, v)

print('\nOrderedDict:')
d = collections.OrderedDict()  # remembers insertion order
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)
