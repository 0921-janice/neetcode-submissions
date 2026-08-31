class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        def backtrack(r):
            if r >= n:
                res.append([''.join(row) for row in board])
                return
            
            for i in range(n):
                if isValid(board, r, i):
                    board[r][i] = 'Q'
                    backtrack(r + 1)
                    board[r][i] = '.'
            
        def isValid(board, r, c):
            # Check vertical column (rows above)
            for i in range(r):
                if board[i][c] == 'Q':
                    return False

            # Check upper-left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check upper-right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True
                
        backtrack(0)
        return res