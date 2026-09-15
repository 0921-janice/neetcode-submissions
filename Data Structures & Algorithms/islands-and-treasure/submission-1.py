class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                row, col = r + dr, c + dc

                if (0<=row<ROWS) and (0 <= col < COLS) and (row,col) not in visited and grid[row][col]!=-1:
                    grid[row][col] = grid[r][c] + 1
                    visited.add((row, col))
                    q.append([row, col])





















