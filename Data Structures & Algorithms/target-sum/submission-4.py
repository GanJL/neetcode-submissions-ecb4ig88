class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, current_sum):

            if i >= len(nums) and current_sum == target:
                return 1

            if i >= len(nums) and current_sum != target:
                return 0

            if (i,current_sum) in memo:
                return memo[(i,current_sum)]

            res = 0

            res += dfs(i+1, current_sum - nums[i])
            res += dfs(i+1, current_sum + nums[i])
            memo[(i,current_sum)] = res

            return res

        return dfs(0,0)


    