class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            CounterS, CounterT = {},{}

            for i in range(len(s)):
                CounterT[t[i]] = CounterT.get(t[i] , 0) + 1 
                CounterS[s[i]] = CounterS.get(s[i] , 0) + 1 
            return CounterT == CounterS

        