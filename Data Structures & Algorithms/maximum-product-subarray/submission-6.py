class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            tmp = curMax
            curMax = max(nums[i] , nums[i] * curMax, nums[i] * curMin)
            curMin = min(nums[i] , nums[i] * tmp, nums[i] * curMin)
            res = max(curMax, res)
        return res