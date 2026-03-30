class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, path, c_sum):
            #base case
            if c_sum == target:
                res.append(path.copy())
                return

            # constraint/invalid path/pruning
            if i >= len(nums) or c_sum > target:
                return

            # choice 1
            path.append(nums[i])
            dfs(i, path, c_sum + nums[i])
            # backtracking
            path.pop()
            # choice 2
            dfs(i+1, path, c_sum)

        dfs(0,[],0)
        return res