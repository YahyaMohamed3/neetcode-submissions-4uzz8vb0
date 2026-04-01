class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False 

        counterS , counterT = {} , {}

        for i in range(len(t)):
            counterS[s[i]] = counterS.get(s[i], 0) + 1
            counterT[t[i]] = counterT.get(t[i], 0) + 1 
        return counterS == counterT
        