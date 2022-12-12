class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2 = 0, 1
        for i in range(1, n+1):
            ans = step1 + step2
            step1 = step2
            step2 = ans
        return ans
       
        
