# Saving structured data with json

# The standard module called json can take Python data hierarchies, 
# and convert them to string representations; this process is called serializing.

# Reconstructing the data from the string representation is called deserializing. 

import json

json.dumps([1, 'simple', 'list'])

# Another variant of the dumps() function, called dump(), 
# simply serializes the object to a text file. 
# So if f is a text file object opened for writing, we can do this:
#f = open('ex15_json.txt', 'w')
# json.dump(x, f)

# To decode the object again, 
# if f is a text file object which has been opened for reading:
# x = json.load(f)

# See also pickle - the pickle module
# Contrary to JSON, pickle is a protocol which allows the serialization of arbitrarily complex Python objects.