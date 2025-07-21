def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, diagonals
    win_conditions = [
        # rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_player_move(board):
    while True:
        try:
            move = input("Enter your move as row and column (e.g. 1 3 for top right): ")
            row, col = map(int, move.split())
            if row in [1,2,3] and col in [1,2,3]:
                if board[row-1][col-1] == " ":
                    return row-1, col-1
                else:
                    print("That cell is already taken. Try again.")
            else:
                print("Row and column must be between 1 and 3. Try again.")
        except:
            print("Invalid input. Please enter two numbers separated by space.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        row, col = get_player_move(board)
        board[row][col] = current_player

        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins! Congrats!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
