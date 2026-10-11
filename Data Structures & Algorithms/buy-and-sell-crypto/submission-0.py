class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute 
        res = 0 
        
        for i in range(len(prices)):
            val = prices[i]

            for j in range(i+1, len(prices)):

                res = max(res, prices[j] - val)

        return res