class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l , r = 0, len(height) - 1
        leftMax , rightMax = height[l], height[r]
        area = 0
        while r > l:
            if leftMax < rightMax:
                area += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l]) 
            else:
                area += rightMax - height[r]
                r -= 1
                rightMax = max(height[r] , rightMax)
        return area
