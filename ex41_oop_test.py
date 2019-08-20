# Learning to Speak Object-Oriented
# python oop_test.py english

import random
# from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
# WORDS = []

WORDS = ['account', 'achiever', 'actor', 'addition', 'adjustment',
'advertisement', 'advice', 'aftermath', 'agreement', 'airplane', 'airport',
'alarm', 'amount', 'amusement', 'angle', 'animal', 'answer', 'ant',
'apparatus', 'apparel', 'apple', 'appliance', 'approval', 'arch', 'argument',
'arithmetic', 'arm', 'army', 'art', 'attack', 'attempt', 'attention',
'attraction', 'aunt', 'authority', 'baby', 'back', 'badge', 'bag', 'bait',
'balance', 'ball', 'balloon', 'banana', 'band', 'base', 'baseball', 'basket',
'basketball', 'bat', 'bath', 'battle', 'bead', 'beam', 'bean', 'bear', 'beast',
'bed','bedroom', 'bee', 'beef', 'beetle', 'beggar', 'beginner', 'behavior',
'belief', 'believe', 'bell', 'berry', 'bike', 'bird', 'birth', 'birthday',
'bit', 'bite', 'blade', 'blood', 'blow', 'board', 'boat', 'body', 'bomb',
'bone', 'book', 'boot', 'border', 'bottle', 'boundary', 'box', 'boy', 'brain',
'brake', 'branch', 'brass', 'bread', 'breakfast', 'breath', 'brick', 'bridge',
'brother', 'brush', 'bubble', 'bucket', 'building', 'bulb', 'bun', 'burn',
'burst', 'business', 'butto']

PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and *** parameters.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}


# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# for word in urlopen(WORD_URL).readlines():
#    WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]  # g = (2**x for x in range(100))
    other_names = random.sample(WORDS, snippet.count("***"))
    # print("Class names:", class_names)
    # print("Other names:", other_names)
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        # That's a Python way of copying a list.
        # You're using the list slice syntax [:] to effectively make a slice from the very first element to the very last one.

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)
    return results


# a, b, c = [1, 5, 10]
# print(a, b, c)
# a, b, c = c, b, a
# print(a, b, c)

# keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
