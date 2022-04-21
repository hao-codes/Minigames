# guess the number game

import random


def guess_number():
    # ask user for upper bound

    print("In this minigame you have to guess the number( the number is a positive integer)")

    while True:
        x = input("Please, set the upper bound for the game: ")
        try:
            x = int(x)
            break
        except ValueError:
            print("Your upper bound is not a integer.")

    # get random number
    random_number = random.randint(0, x)

    # count guesses
    n_guesses = 0
    while n_guesses < 15:
        my_guess = input(f"Guess a number between 0 and {x}: ")

        try:
            my_guess = int(my_guess)
        except ValueError:
            print("Your guess is not a integer. Guess again")
        n_guesses += 1

        if my_guess == random_number:
            print(f"Well done, the number is {random_number}. You only needed {n_guesses} tries.")
            break
        elif my_guess < random_number:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
    if n_guesses == 15:
        print(f"Sorry, you lose. The correct answer was {random_number}")

guess_number()