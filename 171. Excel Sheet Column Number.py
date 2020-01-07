class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        ret = 0
        for i in s:
            ret += 26**(n-1) * (ord(i) -ord('A') + 1)
            n -= 1
        return ret