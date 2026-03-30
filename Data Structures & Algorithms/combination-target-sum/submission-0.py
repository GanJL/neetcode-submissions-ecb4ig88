class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, c_sum):
            #base
            if c_sum == target:
                res.append(path.copy())
                return

            # invalid paths
            if i >= len(nums) or c_sum > target:
                return
            
            path.append(nums[i])
            dfs(i, path, c_sum + nums[i])
            path.pop()
            dfs(i+1, path, c_sum)

        dfs(0,[],0)
        return res