class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #global variables
        pac, atl = set(), set()
        ROW, COL = len(heights), len(heights[0])
        #dfs
        def dfs(r,c,visited,prevHeight):
            if (r<0 or c<0 
                or r == ROW or c == COL 
                or (r,c) in visited
                or prevHeight > heights[r][c]):
                return

            visited.add((r,c))

            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])

            return

        #starting points
        #col
        for c in range(COL):
            dfs(0,c,pac,0)
            dfs(ROW-1,c,atl,0)
        #row
        for r in range(ROW):
            dfs(r,0,pac,0)
            dfs(r,COL-1,atl,0)

        res = []
        pac = list(pac)
        atl = list(atl)
        for i in range(len(pac)):
            for j in range(len(atl)):
                if pac[i] == atl[j]:
                    res.append(list(pac[i]))

        return res




