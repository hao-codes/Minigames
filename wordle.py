# find word with 5 letters

from colorama import Fore, Style  # colors
import csv
import random

# import word dataset
# dataset was downloaded from https://www.kaggle.com/datasets/bcruise/wordle-valid-words

with open('valid_guesses.csv', newline='') as csvfile:
    valid_guesses_reader = csv.reader(csvfile, delimiter=' ')
    valid_guesses = [valid_guess[0] for valid_guess in valid_guesses_reader]
    # for word in valid_guesses_reader:
    #     valid_guesses.append(word[0])

if "word" in valid_guesses:
    valid_guesses.remove("word")

with open('valid_solutions.csv', newline='') as csvfile:
    valid_solutions_reader = csv.reader(csvfile, delimiter=' ')
    # for word in valid_solutions_reader:
    #     valid_solutions.append(word[0])
    valid_solutions = [valid_sol[0] for valid_sol in valid_solutions_reader]

if "word" in valid_solutions:
    valid_solutions.remove("word")


# words = ("stone", "india", "model", "adieu",
#          "crane", "italy", "dutch", "crazy", "lines", "water", "words", "paper", "china", "funny", "theft", "irish")
#

class Wordle:

    def __init__(self):
        self.word = random.choice(valid_solutions)
        # count guesses
        self.n_guesses = 0
        # save guesses
        self.guesses_dict = {
            0: [" "] * 5,
            1: [" "] * 5,
            2: [" "] * 5,
            3: [" "] * 5,
            4: [" "] * 5,
            5: [" "] * 5,
        }

    def drawing_board(self):
        for guess in self.guesses_dict.values():
            print(" | ".join(guess))
            # for char in guess:
            #     print(char)
            print("-----------------")

    def get_user_input(self):
        user_guess = input("Enter a word(5 letters): ")
        while len(user_guess) != 5:
            user_guess = input("Invalid guess, please enter a 5 letter word ")

        while user_guess not in valid_guesses and user_guess not in valid_solutions:
            user_guess = input("Invalid 5 letter word, please enter a valid 5 letter word ")
        user_guess = user_guess.lower()

        for idx, char in enumerate(user_guess):
            if char in self.word:
                if char == self.word[idx]:
                    char = f"{Fore.GREEN}{char}{Style.RESET_ALL}"  # green
                else:
                    char = f"{Fore.YELLOW}{char}{Style.RESET_ALL}"  # yellow
            # put guess in dict
            self.guesses_dict[self.n_guesses][idx] = char

        self.n_guesses += 1
        return user_guess

    def play_game(self):
        self.drawing_board()
        while True:
            user_guess = self.get_user_input()
            self.drawing_board()

            if user_guess == self.word:
                self.drawing_board()
                print(f"N I C E, you won. The word was {self.word}")
                break

            if self.n_guesses > 5:
                self.drawing_board()
                print(f"Sorry, you lost! The correct word was {self.word}. Better luck tomorrow")
                break


game = Wordle()
game.play_game()