class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        base = ord("a")
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - base] +=1
            group[tuple(count)].append(s)
        return list(group.values())


        