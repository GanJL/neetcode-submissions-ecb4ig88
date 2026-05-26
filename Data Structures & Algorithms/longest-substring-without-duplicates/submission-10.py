class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # iterate through list and accumulate distincts
        # have a separate set to track distincts
        # if distinct found, remove from set until distinct is no longer in the set
        # track max set size

        distinct = set()
        l = 0
        maxL = 0
        for i in range(len(s)):
            while s[i] in distinct:
                distinct.remove(s[l])
                l+=1
            distinct.add(s[i])
            maxL = max(maxL, len(distinct))

        return maxL