class Solution:
    def toHex(self, num: int) -> str:
        # how to use operator to do this?
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
            
        d = {i:str(i) for i in range(10)}
        d[10],d[11],d[12],d[13],d[14],d[15] = 'a','b','c','d','e','f'
        
        ans = ""
        while num >= 16:
            ans += d[num%16]
            num //= 16
        if num != 0:
            ans += d[num]
        
        return ans[::-1]
                