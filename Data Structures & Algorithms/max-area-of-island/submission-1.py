class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        maxArea = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            area = 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if ((row in range(ROWS)) and (col in range(COLS)) and grid[row][col] == 1 and (row, col) not in visited):
                        area += 1
                        q.append((row, col))
                        visited.add((row, col))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxArea = max(maxArea, area)

        return maxArea