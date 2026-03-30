class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        num_pad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(i, path):
            #base 
            if i == len(digits):
                if len(digits) == 0:
                    return []
                result.append("".join(path))
                return
            
            for char in num_pad[digits[i]]: #e.g. 2 - a,b,c then 3 - d,e,f
                path.append(char)
                dfs(i+1, path)
                path.pop()
                

        dfs(0,[])
        return result

