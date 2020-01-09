class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0 for i in range(n)]
        dp[0] = min(costs)
        
        for i in range(1,n):
            tem = 0
            # 1 day
            tem = dp[i-1] + costs[0]
            
            # 7 days
            seven = days[i] - 7
            j = i
            while j >= 0 and days[j] > seven: # use a 7-day ticket to cover from day[j] to day[i]
                j -= 1
            if j >= 0:
                tem = min(dp[j] + costs[1], tem)
            else:
                tem = min(costs[1], tem)
            
            # 30 days
            thirty = days[i] - 30
            j = i
            while j >= 0 and days[j] > thirty:
                j -= 1
            if j >= 0:
                tem = min(dp[j] + costs[2], tem)
            else:
                tem = min(costs[2], tem)
            
            dp[i] = tem
            
        return dp[-1]
    
    
            
            
        
        