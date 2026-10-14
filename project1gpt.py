import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

choices = {
    1: "🪨 STONE",
    2: "📄 PAPER",
    3: "✂️ SCISSORS"
}

user_score = 0
computer_score = 0
draw_score = 0
round_no = 1

print(Fore.CYAN + r"""
██████████████████████████████████████████████████████

           🎮 INITIALIZING GAME...

              LOADING.....
                 SUCCESS ✓

         >>>>>> WELCOME PLAYER <<<<<<

██████████████████████████████████████████████████████
""")

while True:

    print(Fore.YELLOW + "=" * 55)
    print(Fore.MAGENTA + f"               ROUND {round_no}")
    print(Fore.YELLOW + "=" * 55)

    print(Fore.CYAN + """
1 = 🪨 STONE
2 = 📄 PAPER
3 = ✂️ SCISSORS
5 = ❌ EXIT
""")

    try:
        user = int(input(Fore.GREEN + "Choose Your Option : "))
    except ValueError:
        print(Fore.RED + "❌ Please enter only numbers!")
        continue

    if user == 5:
        break

    if user not in [1, 2, 3]:
        print(Fore.RED + "❌ Invalid Choice!")
        continue

    print(Fore.YELLOW + "\nReady...")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print(Fore.GREEN + "GO!\n")

    computer = random.randint(1, 3)

    print(Fore.CYAN + f"You Chose      : {choices[user]}")
    print(Fore.CYAN + f"Computer Chose : {choices[computer]}")
    print()

    if user == computer:
        print(Fore.BLUE + "🤝 MATCH DRAW!")
        draw_score += 1

    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):

        print(Fore.GREEN + "🎉 CONGRATULATIONS! YOU WIN!")
        user_score += 1

    else:
        print(Fore.RED + "💻 COMPUTER WINS!")
        computer_score += 1

    print(Fore.YELLOW + "\n------------- SCORE BOARD -------------")
    print(Fore.GREEN + f"😊 User Score     : {user_score}")
    print(Fore.RED + f"🤖 Computer Score : {computer_score}")
    print(Fore.BLUE + f"🤝 Draw           : {draw_score}")
    print(Fore.YELLOW + "---------------------------------------\n")

    round_no += 1

print(Fore.RED + r"""
 ██████╗  █████╗ ██╗     ██╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
""")

print(Fore.YELLOW + "=" * 55)
print(Fore.CYAN + "               FINAL SCORE")
print(Fore.YELLOW + "=" * 55)

print(Fore.GREEN + f"😊 User Score     : {user_score}")
print(Fore.RED + f"🤖 Computer Score : {computer_score}")
print(Fore.BLUE + f"🤝 Draw           : {draw_score}")

print()

if user_score > computer_score:
    print(Fore.GREEN + "🏆 CONGRATULATIONS! YOU WON THE GAME!")
elif computer_score > user_score:
    print(Fore.RED + "💻 COMPUTER WON THE GAME!")
else:
    print(Fore.BLUE + "🤝 THE GAME IS A DRAW!")

print(Fore.CYAN + "\n❤️ Thanks For Playing!")
print(Style.RESET_ALL)