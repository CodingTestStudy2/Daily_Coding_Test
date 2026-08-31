class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        small = prices[0]
        
        for i in range(len(prices)):
            profit = prices[i] - small
            ans = max(ans, profit)
            small = min(small, prices[i])

        return ans

        