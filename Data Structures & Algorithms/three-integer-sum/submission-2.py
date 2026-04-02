class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l , r = i + 1, len(nums) - 1
            while r > l:
                if nums[i] + nums[r] + nums[l] == 0:
                    result.append([nums[i], nums[r], nums[l]])
                    l += 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                elif 0 > nums[i] + nums[r] + nums[l]:
                    l += 1
                else:
                    r -= 1
        return result

                    

                

        
