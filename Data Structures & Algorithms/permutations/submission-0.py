class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans, sol = [], []

        def dfs():
            if len(sol) == len(nums):
                ans.append(sol.copy())
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    dfs()
                    sol.pop()
                
            
        dfs()
        return ans
        