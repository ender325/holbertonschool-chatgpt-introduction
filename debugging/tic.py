#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] \
                and board[0][col] != " ":
            return board[0][col]

    # Check main diagonal
    if board[0][0] == board[1][1] == board[2][2] \
            and board[0][0] != " ":
        return board[0][0]

    # Check opposite diagonal
    if board[0][2] == board[1][1] == board[2][0] \
            and board[0][2] != " ":
        return board[0][2]

    return None


def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input(
                "Enter row (0, 1, or 2) for player " + player + ": "
            ))
            col = int(input(
                "Enter column (0, 1, or 2) for player " + player + ": "
            ))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended.")
            return

        # Validate coordinates
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid coordinates! Enter values from 0 to 2.")
            continue

        # Check whether the selected cell is occupied
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place the current player's mark
        board[row][col] = player

        # Check for a winner before switching players
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Check for a draw
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()