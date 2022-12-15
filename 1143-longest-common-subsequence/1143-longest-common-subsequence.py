class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        row, col = l1+1, l2+1
        
        if l1 == 0 or l2 == 0:
            return 0
        
        memo = [0 for _ in range(col)]
        
        for r in range(1, row):
            prev = memo[0]
            
            for c in range(1, col):
                temp = memo[c]
                
                if text1[r - 1] == text2[c - 1]:
                    memo[c] = prev + 1
                else:
                    memo[c] = max(memo[c - 1], memo[c])
                    
                prev = temp
                
        return memo[-1]
