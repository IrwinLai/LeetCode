class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0 or c == 1:
            return True
        i = 0
        j = int(c**0.5)+1
        
        while(i <= j):
            tem = i*i + j*j
            if tem == c:
                return True
            elif tem < c:
                i += 1
            else:
                j -= 1
        
        return False