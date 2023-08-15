# A simple battleship game.
from random import randint

# Function providing game information that pulls through player name entry.

def game_info(captain_name):
    print("++" + "-" * 60 + "++")
    print("  Welcome to this simple version of Battleships :D \n")
    print("  Game information")
    print("  - The board size is 4 x 4. There is 1 enemy battleship that you"
          " are trying to hunt down.")
    print("  - On each turn enter a number between 0 and 3"
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

    # Input to prompt, validate and enter player name.
    while True:
        captain_name = input("Please enter your name, Captain: \n").strip()
        if len(captain_name) < 2:
            print(f"\nThe name '{captain_name}' is too short."
                "Your name needs to be 2 characters or more. \n")
            continue
        if not captain_name.isalpha():
            print(f"\nThe name '{captain_name}' contains none alphabetic"
                "characters. Please enter a name containing only letters. \n")
            continue
        break
    
    game_info(captain_name)
   

    # Variable to store player turns that can be updated
    board = []

    # Generates an empty board for the game.
    for i in range(0, 4):
        board.append(["0"]*4)

    print_board(board)

    ship_row = row_random(board)
    ship_column = column_random(board)
    
    turns = 10

    # While loop that handles the main game conditions
    while turns > 0:
        # While loop to validate row input
        while True:
            try:
                select_row = int(input("Select a row: "))
            except ValueError:
                output_style("Please enter a number between 0 & 3")
                continue
            else:
                break

        # While loop to validate column input
        while True:
            try:
                select_column = int(input("Select a column: "))
            except ValueError:
                output_style("Please enter a number between 0 & 3")
                continue
            else:
                break

        # Win, outside range and miss condition loops including game over stage.
        if select_row == ship_row and select_column == ship_column:
            output_style("Direct hit! Game over - you win!")
            board[select_row][select_column] = "#"
            print_board(board)
            break
        else:
            if (select_row < 0 or select_row > 3) \
                    or (select_column < 0 or select_column > 3):
                output_style("That's not on the board! Try again...")
            elif (board[select_row][select_column] == "X"):
                output_style("You've already tried that location! Try again...")
            else:
                output_style("That's a miss... you need to improve your aim!")
                board[select_row][select_column] = "X"
                print("Turns remaining: " + str(turns))
                turns -= 1
                if turns == 0:
                    output_style("Game over! You've run out of turns. The correct"
                                f" coordinates were row: {ship_row} & column:"
                                f" {ship_column}.")
                    break

            print_board(board)
main()