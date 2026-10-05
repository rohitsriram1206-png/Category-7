# Local Search for CSP
# Min-Conflicts Algorithm for N-Queens

import random


def conflicts(board, row, col):
    count = 0

    for r in range(len(board)):
        if r == row:
            continue

        c = board[r]

        # Same column
        if c == col:
            count += 1

        # Same diagonal
        if abs(r - row) == abs(c - col):
            count += 1

    return count


def min_conflicts(n, max_steps=10000):

    # Random initial assignment
    board = [random.randint(0, n - 1) for _ in range(n)]

    for step in range(max_steps):

        # Find rows containing conflicts
        conflicted_rows = []

        for row in range(n):
            if conflicts(board, row, board[row]) > 0:
                conflicted_rows.append(row)

        # If there are no conflicts, solution found
        if not conflicted_rows:
            return board

        # Select a random conflicted row
        row = random.choice(conflicted_rows)

        # Calculate conflicts for every possible column
        min_conflict = float('inf')
        best_columns = []

        for col in range(n):

            current_conflicts = conflicts(board, row, col)

            if current_conflicts < min_conflict:
                min_conflict = current_conflicts
                best_columns = [col]

            elif current_conflicts == min_conflict:
                best_columns.append(col)

        # Choose one of the best columns randomly
        board[row] = random.choice(best_columns)

    return None


def print_board(board):

    n = len(board)

    for row in range(n):

        line = ""

        for col in range(n):

            if board[row] == col:
                line += "Q "
            else:
                line += ". "

        print(line)


# Input
n = int(input("Enter number of queens: "))

solution = min_conflicts(n)

if solution:
    print("\nSolution:")
    print_board(solution)

    print("\nQueen positions:")

    for row in range(n):
        print("Row", row + 1, "-> Column", solution[row] + 1)

else:
    print("No solution found.")