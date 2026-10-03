class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            r, l = len(nums) - 1, i + 1
            
            while l < r:
                total = nums[r] + nums[l] + nums[i]
                if total == 0:
                    res.append([nums[r], nums[l], nums[i]])
                    l += 1
                    r -= 1

                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                    while r > l and nums[l] == nums[l - 1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res
