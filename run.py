from random import randint




def start_game():
    
    print("/" + "-" *80 + "/")
    print("Welcome to this terminal version of Battleships :D")
    print("Board size: 4 x 4. Total number of ships: 3")
    print("Enter a row and column coordinate choice to try and sink the computer battleship.")
    print("/" + "-" *80 + "/")
    captain_name = input("Please enter your name, Captain: \n")
    

start_game()

board = []

def print_board(board):
    for i in board:
        print(" ".join(i))

    for i in range(0, 5):
        board.append(["0"]*5)
            
print_board(board)

def row_random(board):
    return randint(0, len(board)-1)
    
def column_random(board):
    return randint(0, len(board)-1)

ship_row = row_random(board)
ship_column = column_random(board)

select_row = int(input("Select a row: "))
select_column = int(input("Select a column: "))

print(select_row)
print(select_column)

if select_row == ship_row and select_column == ship_column:
    print("Hit! You sank an enemy battleship!")
elif (select_row > 5 or select_row < 0) or (select_column > 5 or select_column < 0):
        print("Out of range! Try again...")
elif board[select_row][select_column] == "X":
        print("You've already tried these coordinates... Fire again!")
else:
    print("You missed. Try again...")
    board[select_row][select_column] ="X"
    print_board(board)