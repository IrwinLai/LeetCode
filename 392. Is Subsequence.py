class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        earn = [0 for i in range(len(prices)+1)]
        for i in range(1,len(prices)):
            earn[i] = max(0, earn[i-1]+prices[i] - prices[i-1])
        t = max(earn)
        return t