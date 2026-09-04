class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if ((r in range(ROWS)) and (c in range(COLS)) and (grid[r][c] != -1) and (r,c) not in visited):
                    grid[r][c] = grid[row][col] + 1
                    visited.add((r,c))
                    q.append((r,c))
