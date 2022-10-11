class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        iNum = jNum = float('inf')
        
        for num in nums:
            if num <= iNum:
                iNum = num
            elif num <= jNum:
                jNum = num
            else:
                return True
        return False
    
    