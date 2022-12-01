class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        return (sum(ch in 'aeiouAEIOU' for ch in s[:len(s)//2]) == 
                sum(ch in 'aeiouAEIOU' for ch in s[len(s)//2:]))
    
        