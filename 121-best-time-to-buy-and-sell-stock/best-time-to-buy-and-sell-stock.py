class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        max_prices=0
        min_prices=float("inf")

        for i in range(0,n):
            min_prices=min(min_prices,prices[i])
            
            max_prices=max(max_prices,prices[i]-min_prices)

        return max_prices

    


