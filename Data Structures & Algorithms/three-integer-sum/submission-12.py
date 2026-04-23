class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l , r = i + 1, len(nums) - 1
            while r > l:
                total = nums[r] + nums[i] + nums[l]
                if total == 0:
                    result.append([nums[r] , nums[i], nums[l]])
                    r -= 1
                    l += 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1 
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return result