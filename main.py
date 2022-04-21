# import games

from guess_the_number import guess_number
from rock_paper_scissors import rock_paper_scissors
from wordle import Wordle

while True:
    txt = """Mini Games!!!
    - Guess the number (1)
    - Rock, Paper Scissors (2)
    - Worlde (3)
    - XXXXX(4)

Select a game(press number or 'q' to quit): """
    value = input(txt)

    if value == "1":
        guess_number()
    elif value == "2":
        rock_paper_scissors()
    elif value == "3":
        game = Wordle()
        game.play_game()
    elif value == "4":
        pass
    elif value == "q":
        break
