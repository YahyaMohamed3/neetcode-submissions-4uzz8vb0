class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0 
        l = 0 

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r] , 0) + 1 
            if (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] = freq.get(s[l] , 0) - 1
                l += 1
            res = max(r - l + 1 , res)
        return res 
        
            

            
        