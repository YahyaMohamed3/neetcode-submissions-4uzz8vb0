class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        result = 0 
        while l < r:
            area = min(heights[r] , heights[l]) * (r - l)
            result = max(result, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return result
            
            


