class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in mapping:
                if not stack or stack[-1] != mapping[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        
        return not stack




        # for i in range(len(s)):
        #     if s[i] == "(" or s[i] == "{" or s[i] == "[":
        #         stack.append(s[i])
        #     elif len(stack) > 0:
        #         curr = stack[-1]
        #         if s[i] == ']' and curr == '[':
        #             stack.pop()
        #         elif s[i] == '}' and curr == '{':
        #             stack.pop()
        #         elif s[i] == ')' and curr == '(':
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         return False

        # return len(stack) == 0
        