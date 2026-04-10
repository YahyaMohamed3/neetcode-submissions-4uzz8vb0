class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to the cycle (duplicate number)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow  # or fast, since they meet at the duplicate