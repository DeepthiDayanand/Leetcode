class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        ans = math.inf
        prefix = 0
        index = 0
        total = sum(nums)

        for i in range(len(nums)) :
            prefix += nums[i]
            l=i+1
            r=len(nums)-l
            suffix = total - prefix 
            ad = (prefix // l) - ((suffix//r) if r else 0)
            if abs(ad) < ans :
                ans=abs(ad)
                index=i 
        return index