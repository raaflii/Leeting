def maxProfit(prices):
    # prob = []
    # for i in range (len(prices)):
    #     for j in range(i+1, len(prices)):
    #         if prices[i] < prices[j]:
    #             prob.append(prices[j] - prices[i])

    # if len(prob) != 0: return max(prob)
    # else: return 0
    
    min_price = float('inf')
    max_profit = 0 
    
    for i in prices:
        min_price = min(min_price, i)
        max_profit = max(max_profit, i - min_price)
    
    return max_profit
        

a = maxProfit([7,1,5,3,6,4])
print(a)