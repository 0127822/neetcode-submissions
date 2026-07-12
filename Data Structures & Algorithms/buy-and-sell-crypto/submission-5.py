# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        # loop_length = len(prices)
        # max_profit = 0
        # for i in range(loop_length):
        #     for j in range(i ,loop_length):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l = buy day, r = sell day
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # Found a cheaper day to buy
                l = r

            r += 1

        return max_profit

        
        