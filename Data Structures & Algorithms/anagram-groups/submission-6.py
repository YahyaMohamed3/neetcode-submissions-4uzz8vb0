class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        base = ord("a")

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - base] += 1 
            res[tuple(key)].append(s)
        return list(res.values())

        
            
            
        