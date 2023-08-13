# A simple battleship game.
from random import randint

# Input to prompt and enter player name.
captain_name = input("Please enter your name, Captain: \n")

# Function providing game information that pulls through player name entry.


def game_info():
    print("/" + "-" * 60 + "/")
    print("Welcome to this terminal version of Battleships :D")
    print("Board size: 4 x 4. Total number of enemy battleships: 1")
    print("Enter a row number between 0 and 3")
    print("Enter a column number between 0 and 3")
    print("Sink the enemy ship before you use your 10 turns up")
    print(f"Good luck Captain {captain_name}")
    print("/" + "-" * 60 + "/")


game_info()

# Generates an empty board for the game.
board = []

for i in range(0, 4):
    board.append(["0"]*4)

# Function to print out game board.


def print_board(board):
    for i in board:
        print(" ".join(i))


print_board(board)

# Function to create random row coordinate for battleship


def row_random(board):
    return randint(0, len(board)-1)

# Function to create random column coordinate for battleship


def column_random(board):
    return randint(0, len(board)-1)


ship_row = row_random(board)
ship_column = column_random(board)


# Variable to store player turns that can be updated
turns = 10

# While loop that handles the main game conditions
while turns > 0:
    # While loop to validate row input
    while True:
        try:
            select_row = int(input("Select a row: "))
        except ValueError:
            print("/" + "-" * 40 + "/")
            print("Please enter a number between 0 & 3")
            print("/" + "-" * 40 + "/")
            continue
        else:
            break

    # While loop to validate column input
    while True:
        try:
            select_column = int(input("Select a column: "))
        except ValueError:
            print("/" + "-" * 40 + "/")
            print("Please enter a number between 0 & 3")
            print("/" + "-" * 40 + "/")
            continue
        else:
            break

    # Win, outside range and miss condition loops including game over stage.
    if select_row == ship_row and select_column == ship_column:
        print("/" + "-" * 30 + "/")
        print("Direct hit! Game over - you win!")
        print("/" + "-" * 30 + "/")
        board[select_row][select_column] = "#"
        print_board(board)
        break
    else:
        if (select_row < 0 or select_row > 3) \
                or (select_column < 0 or select_column > 3):
            print("/" + "-" * 35 + "/")
            print("That's not on the board! Try again...")
            print("/" + "-" * 35 + "/")
        elif (board[select_row][select_column] == "X"):
            print("/" + "-" * 50 + "/")
            print("You've already tried that location! Try again...")
            print("/" + "-" * 50 + "/")
        else:
            print("/" + "-" * 26 + "/")
            print("That's a miss! Try again...")
            print("/" + "-" * 26 + "/")
            board[select_row][select_column] = "X"
            turns -= 1
            print("You have " + str(turns) + " turns left")
            if turns == 0:
                print("/" + "-" * 40 + "/")
                print("Game over! You've run out of turns")
                print("/" + "-" * 40 + "/")
                break

        print_board(board)
