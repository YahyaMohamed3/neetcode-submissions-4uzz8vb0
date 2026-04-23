class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            l , r = i + 1, len(nums) - 1 
            while l < r:
                total = nums[r] + nums[l] + nums[i]
                if total == 0:
                    result.append([nums[r] , nums[l] , nums[i]])
                    r -= 1
                    l += 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return result 
                        
                    