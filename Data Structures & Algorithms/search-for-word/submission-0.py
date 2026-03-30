class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #O(m^n)
        lenROW, lenCOL = len(board), len(board[0])
        visited = set()
        def dfs(row,col,path):
            #base case
            if not word.startswith(path):
                return False
            if path == word:
                return True
            #constraints
            if (row == lenROW or col == lenCOL
                or (row,col) in visited or row < 0 or col < 0):
                return False

            visited.add((row,col))
            path += board[row][col]
            #choices
            res = (dfs(row+1,col,path) or 
            dfs(row-1,col,path) or
            dfs(row,col+1,path) or
            dfs(row,col-1,path))

            #backtracking
            visited.remove((row, col))
            return res
            
        for i in range(lenROW):
            for j in range(lenCOL):
                if dfs(i,j,""):
                    return True
        
        return False


        