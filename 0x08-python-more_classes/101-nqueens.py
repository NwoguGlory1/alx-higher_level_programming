#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for x in range(col):
        if board[row][x]:
            return False

    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y]:
            return False

    for x,y in zip(range(row, N, 1), range(col, -1, -1)):
        if board[x][y]:
            return False

    return True

def solve_nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions

def solve_nqueens_util(board, col, N, solutions):
    if col == N:
        solution = [[row, col] for col, row in enumerate(board[0])]
        solutions.append(solution)
        return

    for x in range(N):
        if is_safe(board, x, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = 0

def print_solutions(solutions):
    for solution in solutions:
        print(solution)
        print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
