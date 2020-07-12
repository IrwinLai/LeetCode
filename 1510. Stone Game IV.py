class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0,1]
        sq = []
        for i in range(1,n):
            if i*i <= n:
                sq.append(i*i)
            else:
                break
                
        for i in range(2,n+1):
            tem = 0
            for s in sq:
                if i-s >= 0:
                    if dp[i-s] == 0:
                        tem = 1
                        break
                else:
                    break
            dp.append(tem)
                    
        return dp[n]==1