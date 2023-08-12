from random import randint


board = []

for i in range(0, 5):
        board.append(["0"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))   
         
print_board(board)

def row_random(board):
    return randint(0, len(board)-1)

def column_random(board):
    return randint(0, len(board)-1)

ship_row = row_random(board)
ship_column = column_random(board)
select_row = int(input("Select a row: "))
select_column = int(input("Select a column: "))

ships_remaining = 0

while ships_remaining < 3:
    print(ships_remaining)
    print(ship_row)
    print(ship_column)
    select_row = int(input("Select a row: "))
    select_column = int(input("Select a column: "))    

    if select_row == ship_row and select_column == ship_column:
        ships_remaining += 1
        print("Direct hit! You sunk an enemy battleship.")
        board[select_row][select_column] = "#"
        print_board(board)
    else:
        if (select_row < 0 or select_column > 4) or (select_row < 0 or select_column > 4):
            print("That's not on the board! Try again...")
        elif (board[select_row][select_column] == "X"):
            print("You've already tried that location! Try again...")
        else:
            print("That's a miss! Try again...")
            board[select_row][select_column] = "X"
            print_board(board)
