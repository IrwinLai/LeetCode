class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return num
        
        l = 1
        r = (num+1)//2
        while l < r:
            m = (l + r)//2
            if m*m < num:
                l = m+1
            elif m*m == num:
                return m
            else:
                r = m-1

        return l*l == num