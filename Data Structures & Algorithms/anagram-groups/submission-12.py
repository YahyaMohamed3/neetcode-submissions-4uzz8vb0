class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        base = ord("a")

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - base] += 1
            res[tuple(count)].append(s)
        return list(res.values())

