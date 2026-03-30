class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)): # main pointer iterate thru whole list, skipping as needed

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1 # sub pointer iterate thru remaining list, skipping as needed
            
            while l < r:
                total = nums[l] + nums[r] + nums[i]

                if total == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    
                    while l < r and nums[l+1] == nums[l]: # skip but ensure within sublist
                        l += 1
                    # while l < r and nums[r-1] == nums[r]: # skip but ensure within sublist
                    #     r -= 1

                    l += 1 
                    # r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res




