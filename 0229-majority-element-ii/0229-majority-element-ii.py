class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res1, count1 = None, 0
        res2, count2 = None, 0
        
        for n in nums:
            if res1 == n:
                count1 += 1
            elif res2 == n:
                count2 += 1
                
            elif count1 == 0:
                res1 = n
                count1 += 1
            elif count2 == 0:
                res2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
            
        return[x for x in (res1, res2) if nums.count(x) > len(nums)//3]
                