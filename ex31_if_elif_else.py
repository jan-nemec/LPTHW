# Making Decisions

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
        # Study Drills
        print("""Which sport do you like?
        1. Baseball
        2. Soccer
        3. MMA""")

        sport = input("> ")

        if sport == "1":
            print("I played baseball many years ago.")
            print("Are you good at it?")
            print("1. Yes")
            print("2. No")

            skill = input("> ")

            if skill == "1":
                print("You are great!")
            elif skill == "2":
                print("You are bitch!")
            else:
                print("Did you read the question?")
        else:
            print("I don't like Soccer either Baseball!")

    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is propably better. Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Goodl job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
    # Study Drills
    print("Do you like Python?")
    print("1. I am falling in love with Python!")
    print("2. I hate Python!")

    python = input("> ")

    if python == "1":
        print("Yop, Python is amazing!")
    else:
        print("Are you kidding?")
        print("How old are you?")

        age = int(input("> "))

        if 0 <= age < 10: #age in range(0, 10)
            print("You are kid.")
        elif age < 20:
            print("You are teenager.")
        elif age in range(20, 50):  # 20 <= age < 50
            print("You are senior.")
        else:
            print("You", "are", "old.")
