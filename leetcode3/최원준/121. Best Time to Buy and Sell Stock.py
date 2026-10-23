class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy = float('inf')
        sell = 0
        ans = 0
        for price in prices:
            if price < buy:
                buy = price
                sell = price
            
            sell = max(sell, price)
            ans = max(ans, sell-buy)
            
        return ans
