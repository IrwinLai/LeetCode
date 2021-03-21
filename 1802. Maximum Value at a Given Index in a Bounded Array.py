class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if n == 1:
            return maxSum
        
        def helper1(i,j,m):
            if m >= j-i+1:
                return (m+(m-(j-i)))*(j-i+1)/2
            else:
                return (m+1)*m/2+(j-i+1-m)
                
        
        def helper2(tm):
            tem = helper1(0,index,tm) + helper1(index,n-1,tm) - tm
            if tem <= maxSum:
                return tm
            else:
                return -1
        
        l,r = 1,maxSum-1
        while l < r:
            m = l+(r-l+1)//2
            if helper2(m) == m:
                l = m
            else:
                r = m-1
            
        return l
            