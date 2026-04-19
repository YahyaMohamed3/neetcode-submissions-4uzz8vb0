class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """ 
        build hashmap of each chars last index 
        use two pointers l, r - r is the farthest
        last occurrence of any char seen so far
        when i == r, found the complete parition - record
        its size and start a new one
        """

        hashmap = {c: i for i, c in enumerate(s)}
        res = []
        l = r = 0 

        for i, c in enumerate(s):
            r = max(r, hashmap[c])
            if i == r:
                res.append(r - l + 1)
                l = i + 1
        return res 
        