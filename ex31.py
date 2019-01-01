print("""You enter a dark room with two doorsself.
Do you go through door #1 or door #2?""")

door = input(">")

if door == "1":
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the Cake.")
    print("2. Scream at the bear.")

    bear = input(">")

    if bear == "1":
        print("The bear eats your face. God job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    elif door == "2":
        print("You stare into the endless abyss at the cthulhu's ret")
        print("1.Blueberries.")
        print("2. Yellow Jacket Clothespin.")
        print("3. Understanding revolvers yelling melodies.")
    else:
        print(f"Well, the doing {bear} is probably better.")
        print("Bear runs away.")

    insanity = input(">")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good Job!")

    else:
        print("The insanity rots your eyes into a pool of mud")
        print("Good Job!")
else:
    print("You stumble around and fall on a knife and die. Good Job!")
