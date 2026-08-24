class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i, j = 0, 1

        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)

            else:
                i = j

            j += 1

        return maxProfit
            
































        # l,r = 0, 1
        # maxP = 0
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(maxP, profit)
            
        #     else:
        #         l = r
        #     r+=1
        # return maxP