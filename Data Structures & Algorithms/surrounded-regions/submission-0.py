class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]


        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or board[r][c]=='X' or board[r][c]=='#':
                return

            board[r][c] = '#'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if r==0 or r==(ROWS-1) or c==0 or c==(COLS-1):
                    dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='#':
                    board[r][c]='O'

                elif board[r][c] == 'O':
                    board[r][c] = 'X'
