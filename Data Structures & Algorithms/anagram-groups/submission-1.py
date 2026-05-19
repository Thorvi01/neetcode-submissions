class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) 
        
        for s in strs:
            sortedwords = tuple(sorted(s))
            group[sortedwords].append(s) 

        return list(group.values())
               
        