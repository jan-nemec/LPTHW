# Advanced User Input

# If the user typed "run", and exactly "run", then the game worked.
# If they typed in similar phrases like "run fast" it would fail.
# Now, we'd like to have all of these phrases work the same:
# * open door
# * open the door
# * go THROUGH the door
# * punch bear
# * Punch The Bear in the FACE

# To do this, we're going to write a module that does just that. This module
# have a few classes that work together to handle user input and convert
# it into something your game can work with reliably.

# A simplified version of the English language could include these elements:
# * Words separated by spaces.
# * Sentences composed of the words.
# * Grammar that structures the sentences into meaning.

# Our Game Lexicon
# In our game we have to create a list of allowable words called a "lexicon":
# * Direction words: north, south, east, west, down, up, left, right, back
# * Verbs: go, stop, kill, eat
# * Stop words: the, in, of, from, at, it
# * Nouns: door, bear, princess, cabinet
# * Numbers: any string of 0 through 9 characters

# 1. Breaking up a Sentence
# We've defined a sentence as "words separated by spaces":
stuff = input('> ')
words = stuff.split()

# 2. Lexicon Tuples
# Once we know how to break up a sentence into words, we just have to go
# through the list of words and figure out what "type" they are. For that we
# are going to use a "tuple" - nothing more than a list that you can't modify.
# Tuple is created by putting data inside two () with a comma.
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]
# This creates a pair (TYPE, WORD).
# This is basically the end result. You want to take raw input from the user,
# carve it into words with split, analyze those words to identify their type,
# and finally, make a sentence out of them.

# 3. Scanning Input
# This scanner will take a string of raw input from a user and return a
# sentence that's composed of a list of tuples with the (TOKEN, WORD) pairings.
# If a word isn't part of the lexicon, the it should return the WORD but set
# the TOKEN to an error token, This error tokens will tell users they messed up

# 4. Exceptions and Numbers
# Converting numbers. We're going to cheat and use exceptions. An exception is
# an error that you get from some function you may have run. What happens is
# your function "raises" an exception when it encounters an error, that you
# have to handle that exception.
int("hell")
# The ValueError is an exception that the int() function threw.
# You deal with an exception by using try and except keywords:
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

convert_number(5)
convert_number("hell")

# A Test First Challenge
# For example, if you know how you need to use a new class in another module,
# but you don't quite know how to implement that class yet, then write
# test first.
# This method of writing code is called "pseudo code" and works well if you
# don't know how to implement something, but you can describe it in your
# own words.

# 1. Write a bit of test that fails.
# 2. Write the skeleton function/module/class the test needs.
# 3. Fill the skeleton with comments in your own words explaining how it works.
# 4. Replace the comments with code until the test passes.
# 5. Repeats.

# tests/lexicon_tests.py
# 1. Write the import at the top. Get that to work.
# 2. Create an empty version of the first test case test_directions. Make
# sure that runs.
# 3. Write the first line of the test_diretions test case. Make it fail.
# 4. Go to the lexicon.py file, and create en empty scan function.
# 5. Run the test, and make sure scan is at least running, even though it fails
# 6. Fill in pseudo code comments for how scan should work to make
# test_directions pass.
# 7. Write the code that matches the comments until test_directions passes.
# 8. Go back to test_directions and write the rest of the lines
# 9. Back to scan in lexicon.py and work on it to make this new test code pass.
# 10. Once you've done that you have you first passing test, and you move on to
# the next test.  