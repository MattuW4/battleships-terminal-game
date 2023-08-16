# A simple terminal battleship game.

# Imports for random, time and os
from random import randint

from time import sleep

import os

# Number of rounds the game should run.
NUM_ROUNDS = 12
# Board is a square grid of BOARD_WIDTH x BOARD_WIDTH cells.
BOARD_WIDTH = 5

# Function to clear screen


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function providing game information that pulls through player name entry.


def game_info(captain_name):
    print("++" + "-" * 60 + "++")
    print("  Welcome to this simple version of Battleships :D \n")
    print("  Game information")
    print(f"  - The board size is {BOARD_WIDTH} x {BOARD_WIDTH}."
          " There is 1 enemy battleship that you are trying to hunt down.")
    print(f"  - On each turn enter a number between 0 and {BOARD_WIDTH - 1}"
          " for the row and then the column.")
    print("  - Sink the enemy battleship before you use your 10 turns up! \n")
    print("  Legend for game")
    print("  - 0 = empty space on board")
    print("  - X = location of a missed shot on board")
    print("  - # = direct hit of the enemey ship \n")
    print(f"  Good luck and good hunting, Captain {captain_name}! \n")
    print("++" + "-" * 60 + "++")

# Function to print out game board.


def print_board(board):
    for i in board:
        print(" ".join(i))

# Function to create random row coordinate for battleship


def row_random(board):
    return randint(0, len(board)-1)

# Function to create random column coordinate for battleship


def column_random(board):
    return randint(0, len(board)-1)

# Function for style game condition outputs


def output_style(message):
    border_dash_num = len(message)
    print("")
    print("++" + "-" * border_dash_num + "++")
    print("  " + message)
    print("++" + "-" * border_dash_num + "++")
    print("")

# Main game function


def main():

    clear_screen()

    # Input to prompt, validate and enter player name.
    while True:
        captain_name = input("Please enter your name, Captain: \n").strip()
        if len(captain_name) < 2:
            print(f"\nThe name '{captain_name}' is too short."
                  "Your name needs to be 2 characters or more. \n")
            continue
        if not captain_name.isalpha():
            print(f"\nThe name '{captain_name}' contains none alphabetic"
                  " characters. Please enter a name"
                  " containing only letters. \n")
            continue
        break
    clear_screen()
    game_info(captain_name)

    # Variable to store player turns that can be updated
    turns = NUM_ROUNDS

    board = []

    # Generates an empty board for the game.
    for _ in range(0, BOARD_WIDTH):
        board.append(["0"] * BOARD_WIDTH)

    print_board(board)

    ship_row = row_random(board)
    ship_column = column_random(board)

    # Whle loop that handles the main game conditions
    while turns > 0:
        # While loop to validate row input
        while True:
            try:
                select_row = int(input("Select a row: "))
            except ValueError:
                output_style(f"Please enter a number"
                             " between 0 & {BOARD_WIDTH}")
                continue
            else:
                break

        # While loop to validate column input
        while True:
            try:
                select_column = int(input("Select a column: "))
            except ValueError:
                output_style(f"Please enter a number"
                             " between 0 & {BOARD_WIDTH}")
                continue
            else:
                break

        """
        Win, range and miss condition loops & output.
        Game over stage output.
        """
        if select_row == ship_row and select_column == ship_column:
            clear_screen()
            output_style("Direct hit! The ship was located at"
                         f" row: {ship_row}, column:"
                         f" {ship_column}. You had {turns}"
                         f" turns remaining. Game over - you win :D")
            board[select_row][select_column] = "#"
            print_board(board)
            break
        else:
            if (select_row < 0 or select_row >= BOARD_WIDTH) \
                    or (select_column < 0 or select_column >= BOARD_WIDTH):
                output_style("That's not on the board! Try again...")
                sleep(1.25)
                clear_screen()
                print("Turns remaining: " + str(turns))
            elif (board[select_row][select_column] == "X"):
                output_style("You've already tried that location!"
                             " Try again...")
                sleep(1.25)
                clear_screen()
                print("Turns remaining: " + str(turns))
            else:
                output_style("That's a miss... you need to improve your aim!")
                board[select_row][select_column] = "X"
                turns -= 1
                sleep(1.25)
                clear_screen()
                print("Turns remaining: " + str(turns))
                if turns == 0:
                    clear_screen()
                    output_style("Game over! You've run out of turns."
                                 f" The ship was hiding at"
                                 f" row: {ship_row}, column: {ship_column}.")
                    break

            print_board(board)

    play_again = input("Do you want to play again? Enter y to replay"
                       " or anything else to exit. \n").strip()
    clear_screen()

    if play_again.lower() == "y":
        main()
    else:
        output_style(f"Thank you for playing Captain {captain_name}."
                     " See you on the high seas again soon :D")
        exit()


main()
