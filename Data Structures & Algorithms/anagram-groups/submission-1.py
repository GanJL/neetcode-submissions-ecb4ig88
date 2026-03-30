class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
  
        str_dict = defaultdict(list)

        for string in strs:
            # holder = "".join(sorted(string))
            # str_dict[holder].append(string)
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1

            str_dict[tuple(count)].append(string)

        return list(str_dict.values())


            
        