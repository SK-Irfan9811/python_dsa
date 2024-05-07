def is_possible(board, row, col, digit):
    for i in range(9):
        if board[row][i] == digit:
            return False
        if board[i][col] == digit:
            return False
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit:
            return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                for num in range(1, 10):
                    if is_possible(board, row, col, str(num)):
                        board[row][col] = str(num)
                        if solve_sudoku(board):
                            return True
                        else:
                            board[row][col] = "."
                return False
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
         ]
print(solve_sudoku(board))
print(board)
