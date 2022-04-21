

import random

def rock_paper_scissors():
    print("Let's play Rock Paper Scissors")

    r = "rock"
    p = "paper"
    s = "scissors"

    choices = [r, p, s]

    while True:
        user_choice = input(f"Enter your choice({r}, {p}, {s}): ").lower()
        if user_choice in choices:
            break

        if user_choice not in choices:
            print("Invalid choice, enter your choice again")

    # get random computer choice
    computer = random.choice(choices)
    print(f"User choice: {user_choice}, Computer Choice {computer}")

    # implement game logic

    if user_choice == computer:
        print("Tie")
    elif (user_choice == r and computer == s):
        print("Nice, you won :D\n Rock smashes Scissors")
    elif (user_choice == p and computer == r):
        print("Nice, you won :D\n Paper beats Rock")
    elif (user_choice == s and computer == p):
        print("Nice, you won :D\n  Scissors cuts Paper")
    else:
        print("You lost, better luck next time !")
