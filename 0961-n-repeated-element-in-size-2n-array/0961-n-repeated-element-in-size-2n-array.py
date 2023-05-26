class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        
        for num in nums:
            if num in s:
                return num
            else:
                s.add(num)