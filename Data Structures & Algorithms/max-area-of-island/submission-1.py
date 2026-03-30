class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lenR = len(grid)
        lenC = len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):

            if (r < 0 or 
                c < 0 or 
                r >= lenR or
                c >= lenC or
                grid[r][c] == 0 or
                (r,c) in visited):

                return 0

            visited.add((r,c))

            cur_sum = dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)            

            return 1 + cur_sum

        for row in range(lenR):
            for col in range(lenC):
                res = max(dfs(row,col), res)

        return res