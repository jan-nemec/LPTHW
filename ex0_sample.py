import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

# name = input("Your name? ")
# print("Hello,", name)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Copy"))
r = requests.get("https://coreyms.com")
print(r.status_code)
