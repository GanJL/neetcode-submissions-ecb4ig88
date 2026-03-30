class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def findUnsurroundedOs(row, col):
            #base case
            if row < 0 or col < 0 or row == ROWS or col == COLS or board[row][col] != "O":
                return
            
            board[row][col] = "T"
            
            findUnsurroundedOs(row+1, col)
            findUnsurroundedOs(row-1, col)
            findUnsurroundedOs(row, col+1)
            findUnsurroundedOs(row, col-1)

            return

        # vertical border
        for row in range(ROWS):
            if board[row][0] == "O":
                findUnsurroundedOs(row,0)
            if board[row][COLS-1] == "O":
                findUnsurroundedOs(row,COLS-1)
        # horizontal border
        for col in range(COLS):
            if board[0][col] == "O":
                findUnsurroundedOs(0,col)
            if board[ROWS-1][col] == "O":
                findUnsurroundedOs(ROWS-1,col)
        
        # flip O to X and T to O
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "T":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
                



    



        

