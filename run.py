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

for i in range(0, 4):
        board.append(["0"]*4)

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

turns = 0

while turns < 10:
    select_row = int(input("Select a row: "))
    select_column = int(input("Select a column: "))   

    if select_row == ship_row and select_column == ship_column:
        print("/" + "-" *40 + "/")
        print("Direct hit! Game over - you win!")
        print("/" + "-" *40 + "/")
        board[select_row][select_column] = "#"
        print_board(board)
        break
    else:
        if select_row and select_column >= 4 :
            print("That's not on the board! Try again...")
        elif (board[select_row][select_column] == "X"):
            print("You've already tried that location! Try again...")
        else:
            print("That's a miss! Try again...")
            board[select_row][select_column] = "X"
            turns +=1
            if turns == 10:
                print("/" + "-" *40 + "/")
                print("Game over! You've run out of turns")
                print("/" + "-" *40 + "/")
                break

        print_board(board)
    
