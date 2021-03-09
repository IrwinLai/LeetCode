class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return s == '1'
        
        for i in range(n-1):
            if s[i] == '0' and s[i+1] == '1':
                return False
        return True