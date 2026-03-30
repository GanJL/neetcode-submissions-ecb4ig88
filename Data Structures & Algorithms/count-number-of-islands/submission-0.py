class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        lenRow = len(grid)
        lenCol = len(grid[0])

        # set of tuple
        visited = set()
        def dfs(row,col):

            if (
                row < 0 or
                col < 0 or
                row >= lenRow or 
                col >= lenCol or
                grid[row][col] == "0" or
                (row,col) in visited 
            ):
                return
            
            visited.add((row,col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            


        for i in range(lenRow):
            for j in range(lenCol): 
                if grid[i][j] == "1" and (i,j) not in visited:
                    # first "1" found will add 1 to res and execute DFS,
                    # which will then store all the connected "1" in visited
                    # subsequent "1"s that are not in visited means DFS has not been executed
                    res += 1
                    dfs(i,j)

        return res
