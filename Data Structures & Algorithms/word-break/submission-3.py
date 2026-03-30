class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(i):

            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            for word in wordDict:
                if s.startswith(word,i):
                    if dfs(i+len(word)):
                        # this is not needed for this question, more for standardization for DP
                        memo[i] = True
                        return True
            memo[i] = False           
            return False

        return dfs(0)