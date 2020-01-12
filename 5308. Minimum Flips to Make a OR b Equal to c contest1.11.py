class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        sz = max(len(a),len(b),len(c))
        
        a = (sz-len(a))*'0'+a
        b = (sz-len(b))*'0'+b
        c = (sz-len(c))*'0'+c
        
        res = 0
        for i in range(sz):
            if c[i] == '0':
                if a[i] == '1':
                    res += 1
                if b[i] == '1':
                    res += 1
            else:
                if a[i] == '0' and b[i] == '0':
                    res += 1
        return res