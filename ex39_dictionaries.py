# Dictionaries, Oh Lovely Dictionaries

# A Dictionary (or "dict") is a way to store data just like a list,
# but instead of using only numbers to get the data, you can use almost anything.

# A dictionary is used to map or associate things you want to store to keys you need to get them.
# A dictionary (or dict) is for matching some items (called "keys") to other items (called "values").

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
print(stuff['name'])

print(stuff['height'])

stuff['city'] = "SF"
print(stuff['city'])

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

# print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

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
