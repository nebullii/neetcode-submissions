class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit
        # min_price = float('inf')
        # max_profit = 0
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        # return max_profit