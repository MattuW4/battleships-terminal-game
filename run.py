# A simple battleship game.
from random import randint

# Input to prompt and enter player name.
captain_name = input("Please enter your name, Captain: \n")

# Function providing game information that pulls through player name entry.


def game_info():
    print("/" + "-" * 60 + "/")
    print("Welcome to this simple version of Battleships :D")
    print("- The board size is 4 x 4. There is 1 enemy battleship that you are tyring to hunt down.")
    print("- On each turn enter a number between 0 and 3 for the row and then do the same for the column.")
    print("- Sink the enemy battleship before you use your 10 turns up!")
    print(f"Good luck and good hunting, Captain {captain_name}!")
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
            print("That's a miss... you need to improve your aim!")
            print("/" + "-" * 26 + "/")
            board[select_row][select_column] = "X"
            print("Turns remaining: " + str(turns))
            turns -= 1            
            if turns == 0:
                print("/" + "-" * 40 + "/")
                print("Game over! You've run out of turns")
                print("/" + "-" * 40 + "/")
                break

        print_board(board)
