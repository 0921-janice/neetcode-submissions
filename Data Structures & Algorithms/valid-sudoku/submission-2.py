class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows, cols, squares = defaultdict(list),defaultdict(list),defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    continue

                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3)*3+col//3]:
                    return False

                rows[row].append(board[row][col])
                cols[col].append(board[row][col])
                squares[(row//3)*3+col//3].append(board[row][col])

        return True
                
