### Tic Tac Toe by 2 users ###

## game methods
# print game board
def print_board(board):
    print("\n    1   2   3 \n")
    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("   ---+---+---")
    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("   ---+---+---")
    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")

# check methods(row, column, diagonals) adn for the winner
def check_row(board, row):
    return (board[row][0] == board[row][1] and
            board[row][1] == board[row][2] and
            board[row][0] != " ")
    
def check_column(board, col):
    return (board[0][col] == board[1][col] and
            board[1][col] == board[2][col] and
            board[0][col] != " ")

def check_diagonals(board):
    return (board[0][0] == board[1][1] and
            board[1][1] == board[2][2] and
            board[0][0] != " ") or\
        (board[2][0] == board[1][1] and
         board[1][1] == board[0][2] and
         board[2][0] != " ")


def check_winner(board):
    for i in range(3):
        if check_row(board, i):
            return True
        if check_column(board, i):
            return True
    if check_diagonals(board):
        return True
    return False

# check if the board is full withour winners
def is_board_full(board):
    for item in board:
        if " " in item:
            return False
    return True


def play_user1(board):
    while True:
        row = input("Enter row number: ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Enter row number between 1-3: ")
        row = int(row)
        col = input("Enter column number: ")
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Enter column number between 1-3: ")
        col = int(col)
        if board[row-1][col-1] != " ":
            print("Pick an empty box!")
        else:
            return (row-1, col-1)


def play_user2(board):
    while True:
        row = input("Enter row number: ")
        while not row.isdigit() or int(row) < 1 or int(row) > 3:
            row = input("Enter row number between 1-3: ")
        row = int(row)
        col = input("Enter column number: ")
        while not col.isdigit() or int(col) < 1 or int(col) > 3:
            col = input("Enter column number between 1-3: ")
        col = int(col)
        if board[row-1][col-1] != " ":
            print("Pick an empty box!")
        else:
            return (row-1, col-1)


def start():
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    players = ["X", "O"]
    turn = 0
    
    while not is_board_full(board):
        print_board(board)
        if turn == 0:
            print("Player #1 (X)")
            row, col = play_user1(board)
            board[row][col] = players[turn]
        else:
            print("Player #2 (O)")
            row, col = play_user2(board)
            board[row][col] = players[turn]
        if check_winner(board):
            print_board(board)
            print("Player #1 won!" if turn == 0 else "Player #2 won!")
            break
        turn = 1 - turn
    else:
        print_board(board)
        print("It's a tie!")

# Start the game
start()
