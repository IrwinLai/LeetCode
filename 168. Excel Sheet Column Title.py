class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 0:
             return ""
            
        ans = ""
        
        while n > 0:
            ans += chr((n-1)%26 + ord('A'))
            n = (n-1) // 26
        
        return ans[::-1]