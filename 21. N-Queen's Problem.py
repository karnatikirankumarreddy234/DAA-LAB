def n_queens_easy(n=4):
    def is_safe(row, col, queens):
        for r, c in enumerate(queens):
            # Check column or diagonal conflict
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            result.append(queens.copy())
            return
        for col in range(n):
            if is_safe(row, col, queens):
                queens.append(col)          # place queen
                backtrack(row + 1, queens)  # next row
                queens.pop()                # backtrack

    result = []
    backtrack(0, [])
    
    # Convert to board view
    boards = []
    for sol in result:
        board = [['.' for _ in range(n)] for _ in range(n)]
        for r, c in enumerate(sol):
            board[r][c] = 'Q'
        boards.append([''.join(row) for row in board])
    return boards

# Run it
solutions = n_queens_easy(4)
for board in solutions:
    for row in board:
        print(row)
    print()