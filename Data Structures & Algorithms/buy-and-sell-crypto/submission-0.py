class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profit = float('-inf')

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > 0:
                max_profit = max(profit, max_profit)

        
        return max_profit if max_profit != float('-inf') else 0

        