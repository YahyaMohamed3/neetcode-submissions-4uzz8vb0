class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        base = ord("a")

        for s in strs:
            key = [0] * 26 
            for c in s:
                key[ord(c) - base] +=1
            group[tuple(key)].append(s)
        return list(group.values())
                