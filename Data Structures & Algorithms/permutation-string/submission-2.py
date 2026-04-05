class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        for j in range(len(s1), len(s2)):
            if count1 == count2:
                return True

            count2[ord(s2[j]) - ord('a')] += 1
            count2[ord(s2[j-len(s1)]) - ord('a')] -= 1
            
        return count1 == count2


        # l, r = 0, len(s1) - 1
        
        # while r < len(s2):
        #     temp = list(s1)
        #     l_temp, r_temp = l, r
        #     while l_temp < r_temp+1:
        #         if s2[l_temp] in temp:
        #             temp.remove(s2[l_temp])
        #         l_temp+=1
        #     if not temp:
        #         return True

        #     l+= 1
        #     r+= 1
        # return False
