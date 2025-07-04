def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    winner = None
    
    while winner is None and not is_board_full(board):
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
        else:
            print("That cell is already occupied. Try again.")
    
    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
