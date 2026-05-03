class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i , v in enumerate(nums):
            diff = target - v
            if diff in prevmap:
                return [prevmap[diff] , i]
            prevmap[v] = i
        return -1
            