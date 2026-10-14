import random
"""
1 = stone
2 = paper
3 = scissors 
"""
print(r"""
███████████████████████████████████████████████████

> INITIALIZING GAME...
> LOADING.....
> SUCCESS ✓

>>>>>>   WELCOME PLAYER   <<<<<<

███████████████████████████████████████████████████
""")
while True:
    print("Choose Your Option >>>")
    print("1 = 🪨stone\n2 = 📄paper\n3 = ✂️SCISSORS")

    user = int(input("Please Choose One Option :"))
    computer = random.randint(1, 3)
    

    if (user == 1 and computer == 1):
        print("Draw the match")
    elif (user == 2 and computer == 2):
        print("Draw the match")
    elif(user == 3 and computer == 3):
        print("Draw the match")
    elif(user == 5):
        break
    else:
        if user == 1 and computer == 2:
            print("Computer is win..")
        elif user == 1 and computer == 3:
            print("User is win..")
        elif user == 2 and computer == 1:
            print("User is win..")
        elif user ==2 and computer == 3:
            print("computer is win..")
        elif user == 3 and computer == 1:
            print("computer is win..")
        elif user == 3 and computer == 2:
            print("User is win..")
        else:
            print("Somthing went wrong please try again!")

    if computer == 1:
        print("Computer chuse.. <<🪨STONE>>")
    elif computer == 2:
        print("Computer chuse..<<PAPER>>")
    elif computer == 3:
        print("Computer chuse..<<SEISSIOR>>")

    print("Exit ke liye 5 dabiye")
    print("\n\n")

print(r"""
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝

==============================================================
                      💀 GAME OVER 💀
==============================================================
""")