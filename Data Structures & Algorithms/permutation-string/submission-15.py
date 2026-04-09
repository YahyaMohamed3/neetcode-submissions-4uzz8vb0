class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}
        windowCount = {}
        l = 0 

        for c in s1:
            s1Count[c] = s1Count.get(c , 0) + 1
        
        for r in range(len(s2)):
            windowCount[s2[r]] = windowCount.get(s2[r] , 0) + 1
            if r - l + 1 > len(s1):
                windowCount[s2[l]] -= 1
                if windowCount[s2[l]] == 0:
                    del windowCount[s2[l]]
                l += 1
            if windowCount == s1Count:
                return True
        return False 


             
        