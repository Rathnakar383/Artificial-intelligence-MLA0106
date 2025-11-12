# 8-Queen Problem using Backtracking

N = 8

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, row):
    if row == N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, row, i):
            board[row][i] = 1
            res = solve_nqueens(board, row + 1) or res
            board[row][i] = 0  # Backtrack
    return res

# Main program
board = [[0]*N for _ in range(N)]
if not solve_nqueens(board, 0):
    print("No solution exists")
