class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leftptr = 0
        rightptr = 1
        
        while rightptr < len(prices):
            currentProfit = prices[rightptr] - prices[leftptr]
            if prices[leftptr] < prices[rightptr]:
                profit = max(currentProfit, profit)
            else:
                leftptr = rightptr
            rightptr += 1
        return profit
        
        