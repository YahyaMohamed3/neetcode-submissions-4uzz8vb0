class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for i, v in enumerate(nums):
            missing = target - v
            if missing in prevmap:
                return [prevmap[missing], i]
            else:
                prevmap[v] = i
        return -1