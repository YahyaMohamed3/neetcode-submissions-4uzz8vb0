class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i , v in enumerate(nums):
            x = target - v
            if x in prevmap:
                return [prevmap[x] , i]
            prevmap[v] = i
        return -1