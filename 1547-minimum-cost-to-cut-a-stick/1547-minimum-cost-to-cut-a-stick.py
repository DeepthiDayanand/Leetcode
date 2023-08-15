class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        dp = {}
        
        def dfs(l, r):
            
            if r - l == 1: return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            res = float("inf")
            
            for cut in cuts:
                if l < cut < r:
                    res = min(res, (r - l) + dfs(l, cut) + dfs(cut, r))
                                                               
            dp[(l, r)] = 0 if res == float("inf") else res
            return dp[(l, r)]
            
        return dfs(0, n)
        