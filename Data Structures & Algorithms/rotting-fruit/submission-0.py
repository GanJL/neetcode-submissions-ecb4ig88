class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1],[0,-1],[1,0],[-1,0]]

                for dr,dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or col < 0 or
                        row >= ROW or col >= COL or
                        grid[row][col] != 1
                    ):
                        continue

                    #reusing grid instead of visited set
                    #need to track so that rotten orange does not get enqueued twice
                    #else fresh decrement will be incorrect
                    grid[row][col] = 2
                    q.append((row,col))
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1