class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # dfs return true if island part of cell
        # visited 
        # check every cell

        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]

        visited = set()

        def dfs(row, col):
            
            if (row < 0 or col < 0 or row >= len(grid)
                or col >= len(grid[0]) or grid[row][col] == "0" or (row,col) in visited):
                return
            
            visited.add((row,col))

            for direction in directions:
                dfs(row+direction[0], col+direction[1])

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row,col)
                    count+=1

        return count


