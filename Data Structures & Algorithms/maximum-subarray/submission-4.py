class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxsub, currsum = nums[0], 0
        for n in nums: 
            # if prior sum is negative, reset to current positive
            if currsum < 0:
                currsum = 0
            currsum += n
            # reset based on highest sum to now
            maxsub = max(maxsub, currsum)
        return maxsub
            