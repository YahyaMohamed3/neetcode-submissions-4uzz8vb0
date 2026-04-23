class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1
        result = 0

        while r > l:
            area = min(heights[r], heights[l]) * (r - l)
            result = max(area, result)

            if heights[r] > heights[l]:
                l+= 1
            else:
                r-=1
        return result 

            


