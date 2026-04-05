class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1) - 1
        
        while r < len(s2):
            temp = list(s1)
            l_temp, r_temp = l, r
            while l_temp < r_temp+1:
                if s2[l_temp] in temp:
                    temp.remove(s2[l_temp])
                l_temp+=1
            if not temp:
                return True

            l+= 1
            r+= 1
        return False
