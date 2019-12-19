class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while(n >= 1):
            s += n % 10
            p *= n % 10
            n = n // 10
        return p-s
        
        '''
        n = list(str(n))
        s1 = int(n[0]) 
        s2 = int(n[0])
        for i in n[1:]:
            s1 += int(i)
            s2 *= int(i)
        return s2-s1
        '''