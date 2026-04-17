class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=len(prices)
        max_prices=0
        min_prices=prices[0]
        for i in range(p):
            if prices[i] < min_prices:
                min_prices=prices[i]
            profit = prices[i]-min_prices
            max_prices=max(profit,max_prices)
        return max_prices