# Exercise 23: Strings, Bytes, and Character Encodings

# This exercise will demonstrate:
# 1. How modern computers store human languages for display and processing
#  and how Python this strings.
# 2. How you must ”encode” and ”decode” Python’s strings into a type called bytes.
# 3. How to handle errors in your string and byte handling.

# Today we call a ”byte” a sequence of 8 bits (1s and 0s).
# 00000000 would be 0, 11111111 would be 255, and 00001111 would be 15

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    # The readline function will return an empty string when it reaches 
    # the end of the file and if line simply tests for this empty string. 
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        # If a function is simply a jump to the top where I’ve named it main, 
        # then calling this function at the end of itself would...
        # jump back to the top and run it again. 
        # That would make it loop.


def print_line(line, encoding, errors):
    next_lang = line.strip()  # stripping of the trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, '<===>', cooked_string)

languages = open('languages.txt', encoding='utf-8')

main(languages, input_encoding, error)

# python ex23_strings_bytes_character_encodings_b.py utf-8 strict


# Breaking It
def main2(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line2(line, encoding, errors)
        return main2(language_file, encoding, errors)


def print_line2(line, encoding, errors):
    next_lang = line.strip()
    cooked_string = next_lang.encode(encoding, errors=errors)
    raw_bytes = cooked_string.decode(encoding, errors=errors)

    print(cooked_string, '<===>', raw_bytes)

languages2 = open('languages2.txt', encoding='utf-8')

main2(languages2, input_encoding, error)



# You can try this out in Python
0b1011010 # the number 90 in binary
# 90
ord('Z') # the number based on the letter ’Z’
# 90
chr(90) # I convert the number to the letter ’Z’
#'Z'
