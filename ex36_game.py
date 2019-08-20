# Game
# Exercise 36

from sys import argv, exit

script, name = argv


def fitness_room():
    print('You are in the fitness room. What is your PR for deadlift?')

    choice = int(input('> '))

    # if 0 < choice <= 10:
    if choice in range(0, 11):
        dead('You are too weak...')
    else:
        print('Good job!')
        exit(0)


def kids_room():
    print('There are 2 small kids...Boy and girl.')
    print('What is the name one of them at least?')
    was_there = False

    while True:
        choice = input('> Kid\'s name: ')
        
        if not was_there and choice in ('Filip', 'Natalie'):
            print('The kids are looking at you...')
            print(f'{choice} said: Can you repeat my name?')
            was_there = True
        elif was_there and choice in ('Filip', 'Natalie'):
            hall()
        else:
            #dead('That was not the right name...The kids ate you!')
            print('I got no idea what that means.')


def hall():
    print('You are in the hall.')
    print('There are 3 doors.')
    print('Which one do you take?')

    choice = int(input('> '))

    if choice == 1:
        kids_room()
    elif choice == 2:
        fitness_room()
    elif choice == 3:
        print('3')
        #living_room()
    else:
        dead('There are only 3 doors...')


def dead(why):
    print(f'Reason of the death: {why}')
    exit(0)


def start(name):
    print(f'Hello {name}.')
    print('You are in front of the door.')
    print('You can go in or go out?')
    print('What will you do?')

    choice = input('> ')

    if choice == 'go in':
        hall()
    elif choice == 'go out':
        dead('You bastard! You should not leave the house!')
    else:
        start(name)

print('Let\'s start the game!')
print('-' * 20)
start(name)