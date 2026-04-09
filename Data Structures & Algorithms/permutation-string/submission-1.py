class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = {}
        whash = {}
        l = 0
        for i in range(len(s1)):
            hash1[s1[i]] = hash1.get(s1[i] , 0) + 1
        for r in range(len(s2)):
            whash[s2[r]] = whash.get(s2[r], 0) + 1
            if r - l + 1 > len(s1): 
                whash[s2[l]] -= 1
                if whash[s2[l]] == 0:
                    del whash[s2[l]]
                l += 1
            if whash == hash1:
                return True
        return False

        
        