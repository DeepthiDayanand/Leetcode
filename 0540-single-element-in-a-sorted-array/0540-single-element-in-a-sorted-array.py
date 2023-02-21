class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) // 2
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            index = mid * 2
            if index + 1 >= len(nums) or nums[index] != nums[index + 1]:
                r = mid - 1
                ans = nums[index]
            else:
                l = mid + 1
        return ans
        