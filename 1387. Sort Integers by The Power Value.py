class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def helper(n):
            count = 0
            while n!= 1:
                if n%2 == 0:
                    n = n//2
                else:
                    n = 3*n+1
                count += 1
            return count
        
        l = [i for i in range(lo,hi+1)]
        l.sort(key = lambda x:helper(x))
        print(l)
        return l[k-1]