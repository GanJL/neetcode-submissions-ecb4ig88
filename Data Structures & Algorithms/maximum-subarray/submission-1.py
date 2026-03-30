class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i):

            if i >= len(nums):
                return float('-inf')

            if i in memo:
                return memo[i]

            extend = nums[i] + dfs(i+1)
            start = nums[i]

            memo[i] = max(start, extend)

            return memo[i]

        max_sum = float('-inf')

        for j in range(len(nums)):
            max_sum = max(dfs(j),max_sum)

        return max_sum