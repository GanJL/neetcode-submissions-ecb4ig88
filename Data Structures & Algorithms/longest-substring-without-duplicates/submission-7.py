class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        maxLen = 0
        holder = set()

        for r in range(len(s)):
            while s[r] in holder:
                holder.remove(s[l])
                l += 1 
            holder.add(s[r])
            maxLen = max(maxLen, len(holder))
            
        return maxLen



