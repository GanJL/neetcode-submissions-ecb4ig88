class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
  
        str_dict = defaultdict(list)

        for string in strs:
            holder = "".join(sorted(string))
            str_dict[holder].append(string)

        return list(str_dict.values())


            
        