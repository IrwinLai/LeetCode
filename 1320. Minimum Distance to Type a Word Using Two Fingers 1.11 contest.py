class Solution:
    def minimumDistance(self, word: str) -> int:
        def cost(a,b): # from a to b
            if a == 26:
                return 0
            else:
                return abs(a%6 - b%6) + abs(a//6 - b//6)
            
        dp = [[10000 for i in range(27)] for j in range(len(word))]
        dp[0][26] = 0 # left finger
        dp[0][ord(word[0]) - ord('A')] = 0 # right finger
        
        for i in range(1,len(word)):
            p = ord(word[i-1]) - ord('A')
            c = ord(word[i]) - ord('A')
            for j in range(27):
                dp[i][j] = min(dp[i][j], dp[i-1][j] + cost(p,c)) # same finger
                dp[i][p] = min(dp[i][p], dp[i-1][j] + cost(j,c)) # the other

        return min(dp[len(word)-1])
        
        '''
        def cost(a,b): # from a to b
            if a == 26:
                return 0
            else:
                return abs(a%6 - b%6) + abs(a//6 - b//6)
        def f(word,i,l,r):
            if i >= len(word):
                return 0
            t = ord(word[i]) - ord('A')
            if dp[i][l][r] != -1:
                return dp[i][l][r]
            else:
                dp[i][l][r] = min(f(word,i+1,t,r) + cost(l,t), \
                       f(word,i+1,l,t) + cost(r,t))
                return dp[i][l][r]
        
        dp = [[[-1 for i in range(27)] for j in range(27)] for z in range(len(word))]
        f(word,0,26,26)
        
        return dp[0][26][26]
        '''