class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        

        nums_set = set()

        for n in nums:
            if n in nums_set:
                return True
            else:
                nums_set.add(n)
        return False

        # nums_dict = {}

        # for n in nums:
        #     if n in nums_dict:
        #         return True
        #     else:
        #         nums_dict[n] = "whatever"
        # return False