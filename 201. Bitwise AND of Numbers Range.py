class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        m,n = bin(m)[2:],bin(n)[2:]
        if len(m) != len(n):
            return ans
        
        base = 2**(len(m)-1)
        for i in range(len(m)):
            if m[i] == n[i]:
                if m[i] == '1':
                    ans += base
                base //=2
            else:
                return ans
            
        return ans