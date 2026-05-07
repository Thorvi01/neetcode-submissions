class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """for i in range(1,len(int(str+1))):
            if len(int(strs[i])) == len(int(strs[i+1])) and split(strs[i]) == split(strs[i]):
                print( strs[i],strs[i+1])  
            else:
                print("error")"""
        group = {}
        for s in strs:
            sortedwords = tuple(sorted(s))
            if sortedwords not in group:
                group[sortedwords] =[]
            group[sortedwords].append(s)    

        return list(group.values())                     