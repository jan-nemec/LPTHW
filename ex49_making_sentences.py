# Making Sentences

# ... continue | ex48
# What we should get from our little game lexicon scanner:
# lexicon.scan ("go north")
# [('verb', 'go')]
# lexicon.scan ("kill the princess")
#[('verb', 'kill'), ('stop', 'the'), ('noun', 'princess')]

# A sentence can be a simple structure like:
# Subject Verb Object

# What we want is to turn the list of tuples into a nice Sentence object that
# has subject, verb, and object.

# To do this we need 5 tools:
# 1. A way to loop through the list of scanned words.
# 2. A way to match different types of tuples that we expect in our Subject
# verb Object setup.
# 3. A way to peek at a potential tuple so we can make decisions.
# 4. A way to skip things we do not care about, like stop words.
# 5. A Sentence object to put the results in.

# The Sentence Grammar
# We want to produce a Sentence object that has three attributes:
# Sentence.subject - noun
# Sentence.verb - verb
# Sentence.object - object

# Our parser then has to use the functions we described and, given a scanned
# sentence, convert it into an List of Sentence objects to match the input.

# A Word on Exceptions
# This code demonstrates how to use the ParseError. Notice that it uses classes
# to give it the type of Exception. Also notice the use of the raise keyword
# to raise the exception.

# The Parser Code
# ex48/parser.py

# Playing with The Parser
# from ex48.myparser import *
# x = parse_sentence([('verb', 'run'), ('direction', 'north')])
# x.subject
# x.verb
# x.object
# x = parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')])
# x.subject
# x.verb
# x.objecte