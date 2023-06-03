# Rock Paper Scissors Game

This is a simple implementation of the classic game "Rock Paper Scissors" using Python. The game allows the user to choose between rock, paper, or scissors, and then plays against a computer player that makes a random choice. The game then evaluates the choices and determines the winner, or if it's a tie.

## How to Play

1. Clone or download the repository to your local machine.
2. Open the file `rock_paper_scissors.py` in a Python IDE or editor.
3. Run the file.
4. When prompted, enter your choice by typing 0 for Rock, 1 for Paper, or 2 for Scissors.
5. The computer will randomly choose its move and the game will display the results.

## Code Description

The game is implemented using Python 3 and the built-in `random` module. The game images for rock, paper, and scissors are stored as multi-line strings in the variables `rock`, `paper`, and `scissors`. These images are displayed to the user based on their input. The computer's move is generated using the `random.randint()` function, which generates a random integer between 0 and 2 inclusive.

The game then evaluates the user's and computer's choices and prints the result of the game.
