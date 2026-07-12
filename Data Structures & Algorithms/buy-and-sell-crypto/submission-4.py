class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        loop_length = len(prices)
        max_profit = 0
        for i in range(loop_length):
            for j in range(i ,loop_length):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit


            
        return max_profit


        
        