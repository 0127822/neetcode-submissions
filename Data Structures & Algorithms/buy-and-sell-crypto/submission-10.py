class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop_length = len(prices)
        # max_profit = 0
        # for i in range(loop_length):
        #     for j in range(i ,loop_length):
        #         profit = prices[j] - prices[i]
        #         if profit > max_profit:
        #             max_profit = profit

        # l , r = 0 , 
        # max_profit = 0 

        # while l < r :
        #     print(f"l , r : {l , r}")
        #     profit = prices[r] - prices[l]
        #     print(f"prices[r] ,  prices[l] : {prices[r] , prices[l]}")
        #     print(f"profit :{profit}")
        #     if profit > max_profit:
        #         max_profit = profit
        #         r +=1
        #     else:
        #         l +=1
        
        # return max_profit
        
        buy = 0
        sell = 1
        max_profit = 0
        while(buy<sell and sell<len(prices)):
            profit = prices[sell] - prices[buy]
            max_profit = max(profit , max_profit)
            if profit < 0 :
                buy = sell
            sell +=1

        return max_profit

        

        
        