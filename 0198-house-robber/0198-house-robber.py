class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, current = 0, 0
        for money in nums:
            prev, current = current, max(prev + money, current)
        return current
