class Solution:
    def ways(self, A: List[str], k: int) -> int:
        m, n, MOD = len(A), len(A[0]), 10 ** 9 + 7
        # how many apple is right-down corner
        rem = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                rem[i][j] = rem[i][j+1] + rem[i+1][j] - rem[i+1][j+1] + \
                            (A[i][j] == 'A')
        print(rem)
        @lru_cache(None)
        def dp(i, j, t):
            if rem[i][j] == 0:
                return 0
            if t == 1:
                return 1
            ans = 0
            # vertical
            for nj in range(j+1,n):
                if rem[i][j] - rem[i][nj] >0 :
                    ans = (ans + dp(i,nj,t-1)) % MOD
            #horizontal
            for mi in range(i+1,m):
                if rem[i][j] - rem[mi][j] >0:
                    ans = (ans + dp(mi,j,t-1)) % MOD
            return ans
        
        return dp(0,0,k)
            