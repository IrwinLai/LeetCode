class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s1 = ['1']*n
        s2 = ['0']*n
        for i in range(n):
            if i%2 == 0:
                s1[i] = '0'
                s2[i] = '1'
        c1,c2 = 0,0
        for i in range(n):
            if s[i] != s1[i]:
                c1 += 1
            if s[i] != s2[i]:
                c2 += 1
        return min(c1,c2)