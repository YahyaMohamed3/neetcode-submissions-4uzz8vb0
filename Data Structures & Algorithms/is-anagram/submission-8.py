class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterT, counterS = {}, {}

        for i in range(len(s)):
            counterT[t[i]] = counterT.get(t[i] , 0) + 1
            counterS[s[i]] = counterS.get(s[i], 0) + 1
        return counterT == counterS