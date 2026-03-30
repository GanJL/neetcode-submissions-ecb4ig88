class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        lastLowest = float('inf')
        currentHighest = float('-inf')
        maxDiff = 0

        for i in range(len(prices)):
            if prices[i] < lastLowest:
                lastLowest = prices[i]
                currentHighest = prices[i]
            if prices[i] > currentHighest:
                currentHighest = prices[i]

            maxDiff = max(maxDiff, currentHighest - lastLowest)
        
        return maxDiff

        #   ll ch
        # 7 7   7  0
        # 1 1   1  0
        # 5 1   5  4
        # 3 1   5  4
        # 6 1   6  5
        # 4 1   4  3