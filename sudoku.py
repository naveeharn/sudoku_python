def print_sudoku(board):
    print()
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid_move(board, row, col, num):
    # Check if the number is already in the row or column
    if num in board[row] or num in [board[i][col] for i in range(4)]:
        return False

    # Check if the number is already in the 2x2 subgrid
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num

                        print(f"Checking row {row+1}:", end=" ")
                        print_sudoku(board)
                        input("Press Enter to continue...")

                        print(f"Checking column {col+1}:", end=" ")
                        print_sudoku(board)
                        input("Press Enter to continue...")

                        print(f"Checking 2x2 subgrid:", end=" ")
                        print_sudoku(board)
                        input("Press Enter to continue...")

                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Example 4x4 Sudoku board (0 represents empty cells)
sudoku_board = [
    [0, 0, 3, 0],
    [0, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 0, 0]
]

print("Original Sudoku:")
print_sudoku(sudoku_board)
print("\nSolving Sudoku:")
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_sudoku(sudoku_board)
else:
    print("No solution exists.")
