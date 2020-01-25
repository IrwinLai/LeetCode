class Solution:
    def breakPalindrome(self, p: str) -> str:
        n = len(p)
        if n == 1:
            return ''
        p = list(p)
        if n%2 == 1:
            for i in range(n):
                if i != (n-1)//2:
                    if p[i] != 'a':
                        p[i] = 'a'
                        return ''.join(p)
        else:
            for i in range(n):
                if p[i] != 'a':
                    p[i] = 'a'
                    return ''.join(p)
        p[-1] = 'b'
        return ''.join(p)