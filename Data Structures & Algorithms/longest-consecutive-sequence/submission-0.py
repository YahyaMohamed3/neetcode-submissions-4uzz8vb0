class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0 

        for x in num_set:
            if x - 1 not in num_set:
                y = x 
                while y in num_set:
                     y += 1
                best = max(best, y - x)
        return best


            
             
        