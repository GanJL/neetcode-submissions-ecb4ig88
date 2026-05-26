class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # add all the treasures to bfs queue
        # expand with bfs

        INF = 2**31 - 1

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])): 
                if grid[row][col] == 0:
                    q.append((row,col))

        while q:
            r, c = q.popleft()

            for dr,dc in directions:
                nr, nc = r + dr, c + dc

                if (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and
                    grid[nr][nc] == INF):
                   
                    grid[nr][nc] = grid[r][c] + 1

                    q.append((nr,nc))


            

