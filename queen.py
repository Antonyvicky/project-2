def solveNQueens(N):
    def isSafe(board, row, col):
        # Check if there's a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == N:
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(N):
            if isSafe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    solutions = []
    board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(0)
    return solutions