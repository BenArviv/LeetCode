'''
    Best time to buy and sell stocks:

    You are given an integer array prices where prices[i] is the price of a given stock on the i-th day.
    On each day, you may decide to buy and/or sell the stock.
    You can only hold at most one share of the stock at any time.
    However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.
'''

def maxProfit(prices) -> int:
    profit = 0
    stockVal = 0
    hold = False
    for i in range(0, len(prices)):
        if hold == False:
            if (i < len(prices) - 1) and prices[i] < prices[i + 1]:
                hold = True
                stockVal = prices[i]
        else:
            if prices[i] > stockVal:
                if i < (len(prices) - 1) and prices[i] < prices[i + 1]:
                    if (i + 1) != len(prices) - 1:
                        continue
                    else:
                        profit += prices[i + 1] - stockVal
                        hold = False
                        break
                profit += prices[i] - stockVal
                hold = False
    return profit

# Examples testing
stockList = [1, 2]

print(maxProfit(stockList))
