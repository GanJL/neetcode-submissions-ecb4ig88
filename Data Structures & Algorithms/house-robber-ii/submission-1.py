class Solution:
    def rob(self, nums: List[int]) -> int:
        nums1, nums2 = nums[:-1], nums[1:]

        return max(nums[0], self.helper_rob(nums1), self.helper_rob(nums2))


    def helper_rob(self, nums):
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

