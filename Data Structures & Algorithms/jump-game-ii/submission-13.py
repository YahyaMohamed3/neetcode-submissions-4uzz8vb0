class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l , r +  1):
                farthest = max(farthest, i + nums[i])
            l = r + 1 
            r = farthest
            res += 1
        return res 

"""
I'm using a greedy BFS approach. 
I treat each jump as a level — within the current window of 
reachable positions, I find the farthest I can jump to. 
That farthest point becomes the boundary of my next level. 
Each level costs one jump. 
I keep expanding windows until I reach the end. 
Time complexity is O(n), space is O(1)

"""