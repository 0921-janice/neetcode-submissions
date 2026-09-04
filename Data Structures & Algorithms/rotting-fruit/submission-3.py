class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        fresh = 0
        
        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        minute = 0
        while q and fresh>0:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    
                    if ((r in range(ROWS)) and (c in range(COLS) and grid[r][c]==1 and grid[r][c] != 0)):
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))

            minute += 1

        return minute if fresh == 0 else -1 


