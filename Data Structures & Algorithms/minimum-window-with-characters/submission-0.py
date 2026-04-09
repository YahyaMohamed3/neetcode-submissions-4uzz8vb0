class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t

        countT = {}
        windowCount = {}
        l = 0 

        for c in t:
            countT[c] = countT.get(c , 0) + 1 
        
        have, need = 0, len(countT)
        res = ""
        resLen = float("inf")

        for r in range(len(s)):
            c = s[r]
            windowCount[c] = windowCount.get(c, 0) + 1
            if c in countT and windowCount[c] == countT[c]:
                have += 1
            
            while have == need:
                # save result if this window is smaller
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                # shrink from left
                windowCount[s[l]] -= 1
                if s[l] in countT and windowCount[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        return res

        
        