class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_price = 0
        for price in prices:
            if price - min_price > max_price:
                max_price = price - min_price
            if price < min_price:
                min_price = price
        
        return max_price