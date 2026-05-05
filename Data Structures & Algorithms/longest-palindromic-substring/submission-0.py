class Solution:
    def longestPalindrome(self, s: str) -> str:

        maxLen = 0
        maxIdx = 0
    
        for i in range(len(s)):
            
            #odd
            l,r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    maxIdx = l
                l-= 1
                r+= 1
            
            #even
            l,r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    maxIdx = l
                l-= 1
                r+= 1

        return s[maxIdx:maxIdx + maxLen]


        # longest = ""


        # for i in range(len(s)):
            
        #     #odd
        #     l,r = i, i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l-= 1
        #         r+= 1
            
        #     curr = s[l+1:r]
        #     longest = max(curr, longest, key=len)

        #     #even
        #     l,r = i, i + 1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         l-= 1
        #         r+= 1
            
        #     curr = s[l+1:r]
        #     longest = max(curr, longest, key=len)

        # return longest