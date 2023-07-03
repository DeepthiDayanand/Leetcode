class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setOfNums = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in setOfNums:
                length = 0
                while (length + n) in setOfNums:
                    length +=1
                longest = max(longest, length)
        return longest
                    