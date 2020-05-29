class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def maxsub(l):
            m = l[0]
            t = 0
            for i in range(len(l)):
                if t > 0:
                    t += l[i]
                else:
                    t = l[i]
                m = max(t,m)
            return m
        
        def minsub(l):
            m = l[0]
            t = 0
            for i in range(len(l)):
                if t < 0:
                    t += l[i]
                else:
                    t = l[i]
                m = min(t,m)
            return m
        
        if maxsub(A) < 0:
            return maxsub(A)
        return max(maxsub(A),sum(A)-minsub(A))
        