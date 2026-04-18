class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # first choice
            subset.append(nums[i])
            dfs(i + 1)

            # second choice exclude
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

    


        