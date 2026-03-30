class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = [[-1] * n for _ in range(m)]

        def dfs(r,c):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if memo[r][c] != -1:
                return memo[r][c]

            curr = dfs(r+1,c) + dfs(r,c+1)
            memo[r][c] = curr

            return curr
        
        # this method is only if u want to find the max num of path for each cell
        # max_num = 0
        # for row in range(m):
        #     for col in range(n):
        #         max_num = max(max_num,dfs(row, col))
        # return max_num

        return dfs(0,0)

        