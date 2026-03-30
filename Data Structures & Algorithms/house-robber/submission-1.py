class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # rob1 is before rob2

        # “If I rob this house, how much would I have?”

        # That’s rob1 + current.

        # “If I skip this house, how much do I already have?”

        # That’s rob2.
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp
        return rob2