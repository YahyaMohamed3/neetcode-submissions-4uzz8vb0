class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l , r = 0 , len(height) - 1
        leftMax, rightMax = height[l] , height[r]
        res =0 

        while l < r:
            if rightMax > leftMax:
               res += leftMax - height[l]
               l += 1
               leftMax = max(height[l] , leftMax)
            else:
                res += rightMax - height[r]
                r -= 1 
                rightMax = max(height[r], rightMax)
        return res  



            
        