class Solution1:
    # O[N] Time
    def maxProfit1(self, prices):
        if prices == []:
            return 0

        buyPrice = float('inf')
        sellPrice = 0
        maxProfit = 0

        for price in prices:
            profit = sellPrice - buyPrice
            maxProfit = max(maxProfit, profit)
            buyPrice = min(buyPrice, price)
        return maxProfit


#-----------------------------------------------------------------------
class Solution2:
    # Multiple Transactions but not at the same time
    # VALLEY - PEAK APPROACH
    # O[N] Time
    def maxProfit2(self, prices):
        if prices == []:
            return 0
            
        maxProfit = 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        while i < len(prices)-1:
            # Find the next Valley
            while i < len(prices)-1 and prices[i] >= prices[i+1]:
                i+= 1
            valley = prices[i]

            # Find the next Peak
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]

            maxProfit += peak - valley

        return maxProfit

    # Consecutive values peaks and valleys difference is added at every step
    def maxProfit2(self, prices):
        if prices == []:
            return 0
        
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit




#-----------------------------------------------------------------------
class Solution3:
    def maxProfit3(self, prices):
        if prices == []:
            return 0
        
        leftProfits = [0]*len(prices)
        rightProfits = [0]*len(prices)
        
        # fill the left Profit Array
        leftMin = prices[0]
        for i in range(1, len(prices)-1):
            leftProfits[i] = max(leftProfits[i-1], prices[i] - leftMin)
            leftMin = min(leftMin, prices[i])

        rightMax = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            rightProfits[i] = max(rightProfits[i+1], rightMax - prices[i])
            rightMax = max(rightMax, prices[i])
        
        maxProfit = 0
        for i in range(len(leftProfits)-1):
            maxProfit = max(maxProfit, leftProfits[i]+rightProfits[i+1])

        maxProfit = max(maxProfit, rightProfits[0])

        return maxProfit


