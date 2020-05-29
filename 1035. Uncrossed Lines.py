class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def dp(i,j):
            if i<0 or j<0:
                return 0
            k = 0
            if A[i] == B[j]:
                k = 1
            return max(dp(i-1,j),dp(i,j-1),k+dp(i-1,j-1))
        
        return dp(len(A)-1,len(B)-1)