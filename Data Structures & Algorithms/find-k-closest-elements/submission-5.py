class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = k

        while r < len(arr):
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            r += 1
        return arr[l : l + k]