# We start the parser with the exception we need for a parsing error:

class ParseError(Exception):
    pass    

# This is how you make your own ParseError exception class you can throw.

# Next we need Sentence object:

class Sentece(object):
    
    def __init__(self, subject, verb, obj):
    # remember we take ('noun', 'princess) tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


# We need a function that can peek at a list of words and return what 
# type of word it is.
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None
# We need this function to make decisions about what kind of sentence
# we're dealing with based on what the next word is.

# Then we call another function to consume that word and carry on. The
# match fuction confirms that the expected word is the right type, take it
# off the list, and returns the word.
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None
# I need to peek at words in the list to decide what kind of sentence I'm
# dealing with, and then I need to match those words to create my Sentence.

# I need to skip words that aren't useful to the Sentence. These are words
# labeled 'stop words' ('stop', 'the', 'and', 'a').
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
# If someone types, 'scream at the bear' you get 'scream' and 'bear'.

# We can handle parsing a verb.
def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParseError('Expected a verb next.')

# A similar function handles sentence onjects:
def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParseError('Expected a noun or direction next.')

# Subjects are the similar again, but since we want to handle the implied
# 'player' noun, we have to use peek:
def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParseError('Expected a verb next.')

# Our final parse_sentence function.
def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentece(subj, verb, obj)

