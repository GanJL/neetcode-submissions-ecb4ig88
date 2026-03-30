class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        lenROW, lenCOL = len(board), len(board[0])
        visited = set()

        def dfs(row,col,i):

            if i == len(word):
                return True

            if (row == lenROW or col == lenCOL or
                (row,col) in visited or row < 0 or col < 0 or board[row][col] != word[i]):
                return False

            visited.add((row,col))
            
            res = (dfs(row+1,col,i+1) or 
            dfs(row-1,col,i+1) or
            dfs(row,col+1,i+1) or
            dfs(row,col-1,i+1))

            visited.remove((row, col))
            return res
            
        for i in range(lenROW):
            for j in range(lenCOL):
                if dfs(i,j,0):
                    return True
        
        return False

        # my own: not as optimized

        # def dfs(row,col,path):

        #     if not word.startswith(path):
        #         return False
        #     if path == word:
        #         return True

        #     if (row == lenROW or col == lenCOL
        #         or (row,col) in visited or row < 0 or col < 0):
        #         return False

        #     visited.add((row,col))
        #     path += board[row][col]

        #     res = (dfs(row+1,col,path) or 
        #     dfs(row-1,col,path) or
        #     dfs(row,col+1,path) or
        #     dfs(row,col-1,path))

        #     visited.remove((row, col))
        #     return res
            
        # for i in range(lenROW):
        #     for j in range(lenCOL):
        #         if dfs(i,j,""):
        #             return True
        
        # return False


        