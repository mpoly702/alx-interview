#!/usr/bin/python3
import sys


def solveNQueens(n):
    """Solution for n queens"""
    col = set()
    pos = set()
    neg = set()

    res = []

    board = [[] for _ in range(n)]

    def backtrack(row):
        """Recursion Func"""
        if row == n:
            copy = board.copy()
            res.append(copy)
            return

        for u in range(n):
            if u in col or (row + u) in pos or (row - u) in neg:
                continue

            col.add(u)
            pos.add(row + u)
            neg.add(row - u)

            board[row] = [row, u]

            backtrack(row + 1)

            col.remove(u)
            pos.remove(row + u)
            neg.remove(row - u)
            board[row] = []

    backtrack(0)

    return res


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    boards = solveNQueens(n)
    for board in boards:
        print(board)


if __name__ == "__main__":
    main()
