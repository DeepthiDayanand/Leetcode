class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l = 0
        res = 0
        
        for r, n in enumerate(nums):
            if n == 0:
                l = r + 1
            res = max(res, r-l+1)
        return res
        