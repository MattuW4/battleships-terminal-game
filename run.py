# A simple terminal battleship game.

# Imports for random, time and os
from random import randint
from time import sleep
import os

# Number of rounds the game should run.
NUM_ROUNDS = 12

# Board is a square grid of BOARD_WIDTH x BOARD_WIDTH cells.
BOARD_WIDTH = 5


def clear_screen():
    """Utility function to clear screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def game_info(captain_name):
    """
    Function to create game information section.
        Parameter:
            Takes in board width global variable and captain name.

        Returns:
            Prints to terminal the game information section.
    """
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


def print_board(board):
    """
    Function to print out game board.
        Paramaters:
            Takes in board generation.
        Returns:
            Prints game board to terminal.
    """
    for i in board:
        print(" ".join(i))


def row_random(board):
    """
    Function to create random row coordinate for battleship.
        Paramaters:
            Takes in board generation.
        Returns:
            Random coordinate for row location.
    """
    return randint(0, len(board)-1)


def column_random(board):
    """
    Function to create random column coordinate for battleship.
        Paramaters:
            Takes in board generation.
        Returns:
            Random coordinate for column location.
    """
    return randint(0, len(board)-1)


def output_style(message):
    """
    Function to style game condition outputs.
        Parameters:
            Takes in message content to print.
        Returns:
            Prints out styling around outputs.
    """
    border_dash_num = len(message)
    print("")
    print("++" + "-" * border_dash_num + "++")
    print("  " + message)
    print("++" + "-" * border_dash_num + "++")
    print("")


def main():
    """
    Main game function that runs the main game.
    Parameters:
    - while loops to validate row & column input;
    - local variable to store round numbers in;
    - for loop to generate empty board for the game;
    - variables to store random row & column of ship location;
    - while loop to run main game conditions;
    - while loop to validate row & column input;
    - play again input & exit option;
    Returns:
    - win, range and miss condition loops & outputs;
    - game over stage output;
    """

    # While loop to validate name input
    while True:
        captain_name = input("Please enter your name, Captain:\n").strip()
        if len(captain_name) < 2:
            print(f"\nThe name '{captain_name}' is too short."
                  "Your name needs to be 2 characters or more. \n")
            continue
        clear_screen()
        if not captain_name.isalpha():
            print(f"\nThe name '{captain_name}' contains none alphabetic"
                  " characters. Please enter a name"
                  " containing only letters. \n")
            continue
        break

    game_info(captain_name)

    # Variables to store rounds and board
    turns = NUM_ROUNDS

    board = []

    # For loop to generate board
    for _ in range(0, BOARD_WIDTH):
        board.append(["0"] * BOARD_WIDTH)

    print_board(board)

    # Variables calling random row & column functions
    ship_row = row_random(board)
    ship_column = column_random(board)

    # While loop for main game conditions
    while turns > 0:
        # While loop to validate row input for integer
        while True:
            try:
                select_row = int(input("Select a row:\n"))
            except ValueError:
                output_style(f"Please enter a whole number"
                             f" between 0 & {BOARD_WIDTH}")
                continue
            else:
                break

        # While loop to validate column input for integer
        while True:
            try:
                select_column = int(input("Select a column:\n"))
            except ValueError:
                output_style(f"Please enter a whole number"
                             f" between 0 & {BOARD_WIDTH}")
                continue
            else:
                break

        # If/else loop to determine hit, out of range, miss or game over
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
                sleep(1)
                clear_screen()
                print("Turns remaining: " + str(turns))
            elif (board[select_row][select_column] == "X"):
                output_style("You've already tried that location!"
                             " Try again...")
                sleep(1)
                clear_screen()
                print("Turns remaining: " + str(turns))
            else:
                output_style("That's a miss... you need to improve your aim!")
                board[select_row][select_column] = "X"
                turns -= 1
                sleep(1)
                clear_screen()
                print("Turns remaining: " + str(turns))
                if turns == 0:
                    clear_screen()
                    output_style("Game over! You've run out of turns."
                                 f" The ship was hiding at"
                                 f" row: {ship_row}, column: {ship_column}.")
                    break

            print_board(board)

    # If/Else loop for play again or exit
    play_again = input("\n Do you want to play again? Enter 'y' to replay"
                       " or anything else to exit.\n").strip()
    clear_screen()

    if play_again.lower() == "y":
        main()
    else:
        output_style(f"Thank you for playing Captain {captain_name}."
                     " See you on the high seas again soon :D")
        exit()


# Execute main function
main()
