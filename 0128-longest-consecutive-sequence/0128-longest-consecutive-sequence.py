class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setOfNums = set(nums)
        sequence = 0
        
        for n in nums:
            if (n - 1) not in setOfNums:
                length = 0
                while(n + length) in setOfNums:
                    length += 1
                sequence = max(sequence, length)
        return sequence
        
        