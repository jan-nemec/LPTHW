# Homework
from sys import exit


# intro
def intro(name):
    while(True):
        print("You are in the room.\nThere is door in front of you, to your right and left.\nYou can also leave.")
        print("Which one do you take?")

        choice = input("> options: left, right, in front, leave: ")

        if choice == "left":
            boys_room()
        elif choice == "in front":
            kids_room()
        elif choice == "right":
            girls_room()
        elif choice == "leave":
            leave(name)
        else:
            print("Please choose one from the options.")

# boys_room

# girls_room

# kids_room


# leave
def leave(name):
    print(f"Would you like to stay with us and enjoy beautiful night, {name}?!")
    asked = False

    while(True):
        choice = input("> options: yes, no: ")

        if choice == "yes" and not asked:
            start()
        if choice == "no" and not asked:
            print("Are you sure? It's your last chance.")
            asked = True
        elif choice == "yes" and asked:
            dead("You bastard, go home to your mom!")
        else:
            print("What did you answer?")


# dead
def dead(message):
    print(message)
    exit(0)


# start
def start():
    print("What's your name? ", end=" ")
    name = input()
    #name = input("What's your name? ")

    print(f"Hi, {name}!")
    print("Welcome in our amazing game...")

    intro(name)

start()