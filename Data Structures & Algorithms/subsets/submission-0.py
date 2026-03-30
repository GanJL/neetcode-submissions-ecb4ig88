class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        lenNums = len(nums)
        def dfs(i,path):
            #base case
            if i == lenNums:
                res.append(path.copy())
                return
            #constraint

            #choice
            path.append(nums[i])
            dfs(i+1, path)
            #backtrack
            path.pop()
            #choice
            dfs(i+1, path)
        
        dfs(0,[])
        return res