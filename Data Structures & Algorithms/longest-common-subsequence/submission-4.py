class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        def dfs(i,j):

            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                res = 1 + dfs(i+1, j+1)
            else:
                res = max(dfs(i+1, j), dfs(i, j+1))

            memo[(i, j)] = res
            return res

        return dfs(0,0)

        # 0 -- text1 = c, text2 = c, + 1
        # 1 -- text1 = a, text2 = c
        # 2 -- text1 = a, text2 = r
        # 3 -- text1 = a, text2 = a, + 1
        # 4 -- text1 = t, text2 = c
        # 5 -- text1 = t, text2 = r
        # 6 -- text1 = t, text2 = a
        # 7 -- text1 = t, text2 = b
        # 8 -- text1 = t, text2 = t, + 1
        # 9 -- return 0

        # 0 -- text1 = p, text2 = v
        # 1 -- text1 = p, text2 = o
        # 2 -- text1 = p, text2 = z
        # 3 -- text1 = p, text2 = s
        # 4 -- text1 = p, text2 = h
        # 5 -- text1 = t, text2 = r
        # 6 -- text1 = t, text2 = a
        # 7 -- text1 = t, text2 = b
        # 8 -- text1 = t, text2 = t, + 1
        # 9 -- return 0


