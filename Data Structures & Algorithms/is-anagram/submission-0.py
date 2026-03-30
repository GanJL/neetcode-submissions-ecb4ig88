class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        anagram = {}

        for _s in s:
            if _s in anagram:
                anagram[_s] += 1
            else:
                anagram[_s] = 1

        for _t in t:
            if _t in anagram and anagram[_t] > 0:
                anagram[_t] -= 1
            else:
                return False

        return True
        
