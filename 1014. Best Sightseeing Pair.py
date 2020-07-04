class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        left,ans = 0,0
        for right in range(1,len(A)):
            ans = max(ans, A[left]+left+A[right]-right)
            if left+A[left] < right+A[right]:
                left = right
        return ans
                
            
        '''
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res
        '''