# Exercise 14: Prompting and Passing
from sys import argv

script, user_name, age = argv
prompt = '> Please answer: '

print(f"Hi {user_name}. You are {age} years old. I am the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# We'll use input slightly differently by having it print a simple > prompt
# We make a variable prompt that is set to the prompt we want,
# and we give that to input instead of typing it over and over.
# Now if we want to make the prompt something else,
# we just change it in this one spot and rerun the script. Very handy.
likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)
lives = input(f'Where do you live {user_name}? ')

print("What kind of computer do you have?")
computer = input(prompt)

# combined a """ style multiline string with the {} format activator
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer}. Nice
""")